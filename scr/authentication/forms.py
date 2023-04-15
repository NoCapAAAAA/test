from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

user_model = get_user_model()


class RegisterForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

    class Meta:
        model = user_model
        fields = ('username', 'email', 'first_name', 'last_name', 'middle_name', 'gender', 'phone_number', 'password1', 'password2')


class LoginForm(auth_forms.AuthenticationForm):
    pass


class CustomUserCreationForm(UserCreationForm):
    # todo check if I need this form
    class Meta:
        model = user_model
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    # todo
    class Meta:
        model = user_model
        fields = ('email',)