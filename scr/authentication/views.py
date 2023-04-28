from django.views.generic import FormView
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.conf import settings
from django.shortcuts import redirect
from .forms import (LoginForm, RegisterForm, UserForgotPasswordForm, UserSetNewPasswordForm)
from django.contrib.auth.models import Group
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

User = get_user_model()


class LoginView(FormView):
    template_name = 'sing_in.html'
    form_class = LoginForm
    success_url = settings.LOGIN_REDIRECT_URL

    def get_success_url(self) -> str:

        users_in_group = Group.objects.get(name="Директор").user_set.all()
        users_in_group2 = Group.objects.get(name="Менеджер").user_set.all()

        if self.request.user in users_in_group:
            return '/staff/director/'
        elif self.request.user in users_in_group2:
            return '/staff/manager/'
        else:

            return super().get_success_url()

    def form_valid(self, form):
        user = authenticate(self.request, **form.cleaned_data)
        login(self.request, user)
        return super().form_valid(form)


class RegisterView(FormView):
    template_name = 'sing_up.html'
    form_class = RegisterForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('/')


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'user_password_reset.html'
    success_url = reverse_lazy('home')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'password_subject_reset_mail.txt'
    email_template_name = 'password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'user_password_set_new.html'
    success_url = reverse_lazy('home')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context