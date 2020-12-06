from django import forms
from django.contrib.auth.models import User
from .models import PizzaShop


# Мы используем model User, поэтому ModelForm вместо Form
class UserForm(forms.ModelForm):
    """Владелец пиццерии"""
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class PizzaShopForm(forms.ModelForm):
    """Пиццерия"""

    class Meta:
        model = PizzaShop
        fields = ('name', 'phone', 'address', 'logo')