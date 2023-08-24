from django.urls import path

from users.views import (LoginView, LogoutView, RegisterView, UserConfirmationSentView, UserConfirmEmailView,
                         UserConfirmedView, UserConfirmationFailedView, UserUpdateView)
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    path('email_confirmation_sent/', UserConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm_email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email_confirmed/', UserConfirmedView.as_view(), name='email_confirmed'),
    path('email_confirmation_failed/', UserConfirmationFailedView.as_view(), name='email_confirmation_failed'),

    path('profile/', UserUpdateView.as_view(), name='profile'),
]
