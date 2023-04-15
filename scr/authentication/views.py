from django.views.generic import FormView
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.conf import settings
from django.shortcuts import redirect
from .forms import (LoginForm, RegisterForm)
from django.contrib.auth.models import Group

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