from django.urls import path
from . import views as v

urlpatterns = [
    path('login/', v.LoginView.as_view(), name='sing_in'),
    path('sing-up/', v.RegisterView.as_view(), name='sing_up'),
    path('logout/', v.logout_view, name='logout'),
    path('password-reset/', v.UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', v.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
