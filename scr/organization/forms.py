from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms
from core import models as m
from django.contrib.auth.forms import UserCreationForm
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
        fields = ('username', 'email', 'first_name', 'last_name', 'middle_name', 'gender', 'phone_number', 'password1',
                  'password2')
        help_texts = {
            'username': None,
            'password1': None,
        }


class SettingsProfile(auth_forms.UserChangeForm):
    password = None

    class Meta:
        model = user_model
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name', 'phone_number', 'gender', 'photo', 'groups')
        help_texts = {
            'username': None,
        }


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['size'].disabled = True
        self.fields['period'].disabled = True
        self.fields['adress'].disabled = True
        self.fields['payed_at'].disabled = True
        self.fields['datastart'].disabled = True
        self.fields['datafinish'].disabled = True
        self.fields['price'].disabled = True
        self.fields['quantity'].disabled = True


class CreateOrderForm(forms.ModelForm):
    price = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    user = forms.ModelChoiceField(queryset=get_user_model().objects.order_by('-pk')[:5])
    payed_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = m.OrderStorage
        fields = '__all__'


"""
Работа с сотрудниками
"""


class CreateEmployeeForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    class Meta:
        model = user_model
        fields = '__all__'


