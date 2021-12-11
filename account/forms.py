from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

# registeration form


class SignupForm(UserCreationForm):
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Confirm Password', 'size': "50"}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password', 'size': "50"}))
    # profile_image = forms.FileField()

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email']
        labels = {'username': 'Username ', 'first_name': 'First  name',
                  'last_name': 'Last name', 'email': 'Email', }
        widgets = {'username': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your Username', 'size': "50", }, ), 'first_name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name ', 'size': "50", 'required': True}, ), 'last_name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your Last name', 'size': "50", 'required': True},), 'email': forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your Email', 'size': "50", 'required': True},)}


class EditUserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'date_joined', 'last_login']
        labels = {'username': 'Enter Username ', 'first_name': 'Enter Your first  name',
                  'last_name': 'Enter Your last name', 'email': 'Enter Your Email', }
        exclude = ['username']


class EditAdminProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = '__all__'
        labels = {'username': 'Enter Username ', 'first_name': 'Enter Your first  name',
                  'last_name': 'Enter Your last name', 'email': 'Enter Your Email', }
        exclude = ['groups', 'user_permissions', 'username']
