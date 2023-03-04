import datetime
import secrets

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView, ListView

from config import settings
from users.forms import CustomEditUserForm, NewCustomEditUserForm
from users.models import User


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class UserCreateProfileView(CreateView):
    model = User
    form_class = NewCustomEditUserForm
    template_name = 'users/user_create.html'
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            ###
            self.object.token = make_password(self.object.password).replace('/', '')
            self.object.token_created = datetime.datetime.now().astimezone()
            self.object.is_active = False
            ###
            self.object.set_password(form.data.get('password'))
            self.object.save()
            ###
            send_mail(
                subject='Активация',
                message=f'http://localhost:8000/users/activate/{self.object.token}/',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email],

            )
        return super().form_valid(form)


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/login.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('djank:distribution')

    def get_object(self, queryset=None):
        return self.request.user


def user_activation(request, token):
    u = User.objects.filter(token=token).first()
    if u:
        u.is_active = True
        u.save()
    return redirect('http://localhost:8000')


def reset_password(request):
    if request.method == 'POST':

        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            mail = password_reset_form.cleaned_data['email']

            try:
                user = User.objects.get(email=mail)

            except Exception:
                user = False

            if user:
                new_password = secrets.token_urlsafe(18)[:15]
                user.set_password(new_password)
                user.save()
                send_mail(
                    subject='Смена пароля',
                    message=f'Пароль успешно обновлен, для входа в аккаун используйте следующие дынные:\nПочта: {mail}\nПароль: {new_password}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[mail],
                    fail_silently=False
                )
                return redirect('users:login')
    return render(request, 'users/password_recovery.html')


class MyPasswordChangeView(PasswordChangeView):
    success_url = '/'
    template_name = 'users/change_passwd.html'


class UserListView(UserPassesTestMixin, ListView):
    model = User
    form_class = CustomEditUserForm

    def test_func(self):
        return self.request.user.is_staff


@user_passes_test(lambda u: u.is_staff)
def client_ban(requests, pk):
    distribution_item = get_object_or_404(User, pk=pk)
    if distribution_item.is_active:
        distribution_item.is_active = False
    else:
        distribution_item.is_active = True
    distribution_item.save()
    return redirect(reverse('users:user_list'))