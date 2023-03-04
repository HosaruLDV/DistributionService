from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from djank.forms import ClientForm, MessageForm, DistributionForm
from djank.models import Client, Message, DistributionList


# Create your views here.

class ClientListView(ListView):
    model = Client

    def get_queryset(self):
        if self.request.user.is_staff:
            return Client.objects.all()
        else:
            return Client.objects.filter(owner=self.request.user)


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('djank:client')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super(ClientCreateView, self).form_valid(form)


class ClientDeleteView(UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('djank:client')

    def test_func(self):
        client = self.get_object()
        return client.owner == self.request.user


class ClientDetailView(UserPassesTestMixin, DetailView):
    model = Client
    form_class = ClientForm

    def test_func(self):
        client = self.get_object()
        return client.owner == self.request.user


class ClientUpdateView(UserPassesTestMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('djank:client')

    def test_func(self):
        client = self.get_object()
        return client.owner == self.request.user


class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        if self.request.user.is_staff:
            return Message.objects.all()
        else:
            return Message.objects.filter(owner=self.request.user)


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('djank:message')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super(MessageCreateView, self).form_valid(form)


class MessageDeleteView(UserPassesTestMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('djank:message')

    def test_func(self):
        message = self.get_object()
        return message.owner == self.request.user


class MessageDetailView(UserPassesTestMixin, DetailView):
    model = Message
    form_class = MessageForm

    def test_func(self):
        message = self.get_object()
        return message.owner == self.request.user


class MessageUpdateView(UserPassesTestMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('djank:message')

    def test_func(self):
        message = self.get_object()
        return message.owner == self.request.user


class DistributionListView(ListView):
    model = DistributionList

    def get_queryset(self):
        if self.request.user.is_staff:
            return DistributionList.objects.all()
        else:
            return DistributionList.objects.filter(owner=self.request.user)


class DistributionCreateView(CreateView):
    model = DistributionList
    form_class = DistributionForm
    success_url = reverse_lazy('djank:distribution')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super(DistributionCreateView, self).form_valid(form)


class DistributionUpdateView(UserPassesTestMixin, UpdateView):
    model = DistributionList
    form_class = DistributionForm
    success_url = reverse_lazy('djank:distribution')

    def test_func(self):
        distribution = self.get_object()
        return distribution.owner == self.request.user or self.request.user.is_staff


class DistributionDeleteView(UserPassesTestMixin, DeleteView):
    model = DistributionList
    success_url = reverse_lazy('djank:distribution')

    def test_func(self):
        distribution = self.get_object()
        return distribution.owner == self.request.user or self.request.user.is_staff


class DistributionDetailView(UserPassesTestMixin, DetailView):
    model = DistributionList
    form_class = DistributionForm

    def test_func(self):
        distribution = self.get_object()
        return distribution.owner == self.request.user or self.request.user.is_staff


@user_passes_test(lambda u: u.is_staff)
def change_distribution_status(requests, pk):
    distribution_item = get_object_or_404(DistributionList, pk=pk)
    if distribution_item.status == DistributionList.STATUS_LAUNCHED:
        distribution_item.status = DistributionList.STATUS_COMPLETED
    distribution_item.save()
    return redirect(reverse('djank:distribution'))
