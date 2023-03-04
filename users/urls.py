from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import CustomLoginView, UserEditProfileView, UserCreateProfileView, user_activation, reset_password, \
    MyPasswordChangeView, UserListView, client_ban

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path('register/', UserCreateProfileView.as_view(), name='register'),
    path('activate/<str:token>/', user_activation, name='activate'),
    path('reset_password/', reset_password, name='reset_password'),
    path('password/', MyPasswordChangeView.as_view(), name='change_passwd'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('user_baned/<int:pk>/',client_ban, name='user_baned')
]