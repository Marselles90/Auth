from django import forms
from django.contrib.auth.models import User
from .models import Customer, Transaction


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
    

class FormCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'balance' ]


class FormTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender', 'reseiver', 'amount']