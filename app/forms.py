from django.forms import ModelForm, Textarea
from django.forms.widgets import Widget
from .models import *
from django import forms

from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

        widgets = {     
            'username' : forms.TextInput(),
            'email' : forms.EmailInput(),
            'first_name' : forms.TextInput(),
            'last_name' : forms.TextInput(),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

        widgets = {     
            'username' : forms.TextInput(),
            'email' : forms.EmailInput(),
            'first_name' : forms.TextInput(),
            'last_name' : forms.TextInput(),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
        }