from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, UserVerificationView, send_new_password, \
    UserListView, UserUpdateViewFromList

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/', UserVerificationView.as_view(), name='verification'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/send_new_password/', send_new_password, name='send_new_password'),
    path('list/', UserListView.as_view(), name='list'),
    path('edit/<int:pk>/', UserUpdateViewFromList.as_view(), name='edit'),

]

