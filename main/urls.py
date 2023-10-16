from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import home, MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView, \
    MailingDeleteView, LogListView,MessageCreateView,MessageListView,MessageUpdateView,MessageDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('list', MailingListView.as_view(), name='list'),
    path('create/', MailingCreateView.as_view(), name='create'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
    path('log', LogListView.as_view(), name='log_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_list', MessageListView.as_view(), name='message_list'),
    path('message_edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
]

