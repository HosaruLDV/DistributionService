from django.urls import path

from blog.views import home
from djank.apps import DjankConfig
from djank.views import *

app_name = DjankConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('distribution_list/', DistributionListView.as_view(), name='distribution'),
    path('client/', ClientListView.as_view(), name='client'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('message/', MessageListView.as_view(), name='message'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('distribution_create/', DistributionCreateView.as_view(), name='distribution_create'),
    path('distribution_update/<int:pk>/', DistributionUpdateView.as_view(), name='distribution_update'),
    path('distribution_delete/<int:pk>/', DistributionDeleteView.as_view(), name='distribution_delete'),
    path('distribution_detail/<int:pk>/', DistributionDetailView.as_view(), name='distribution_detail'),
    path('status/<int:pk>', change_distribution_status, name='status'),

]