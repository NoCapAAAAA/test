from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms
from core import models as m
user_model = get_user_model()

"""
Работа с пользовательскими данными
"""


class CreateUserForm(auth_forms.UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

    class Meta:
        model = user_model
        fields = '__all__'

class SettingsProfile(auth_forms.UserChangeForm):
    password = None

    class Meta:
        model = user_model
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name', 'phone_number', 'gender', 'photo')


class CustomPasswordChangeForm(auth_forms.PasswordChangeForm):
    def __init__(self, instance, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)


"""
Работа с заказами
"""


class UpdateOrderDir(forms.ModelForm):

    class Meta:
        model = m.OrderStorage
        fields = '__all__'


class OrderCreate(forms.ModelForm):
    price = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(),)

    class Meta:
        model = m.OrderStorage
        fields = '__all__'