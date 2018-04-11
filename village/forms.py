from django import forms
from .models import Child
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['child_name', 'child_age', 'gender', 'location', 'affliction', 'details']

# class ToyForm(forms.ModelForm):
#     class Meta:
#         model = Toy
#         fields = ['name',]

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Email is required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
