from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import home, MailingListView,MailingCreateView,MailingDetailView,MailingUpdateView,MailingDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='home'),
    path('create/', MailingCreateView.as_view(), name='create'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
]

