from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].empty_label = "Таңдаңыз"

    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Registration
        fields = '__all__'

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class EmailForm(forms.Form):
    email = forms.EmailField(label='Пайдаланушы аты')
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)

