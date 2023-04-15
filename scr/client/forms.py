from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms
import core.models as m

user_model = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    password = None

    class Meta:
        model = user_model
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name',
                  'phone_number', 'gender', 'photo')


class CustomPasswordChangeForm(auth_forms.PasswordChangeForm):
    def __init__(self, instance, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)


class OrderCreateForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(), widget=forms.HiddenInput())
    is_payed = forms.BooleanField(required=False, widget=forms.HiddenInput())
    status = forms.IntegerField(widget=forms.HiddenInput())
    payed_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    price = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = m.OrderStorage
        fields = '__all__'