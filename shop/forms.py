from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from shop.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')
    address = forms.CharField(max_length=254, help_text='Enter your address')
    phone = forms.CharField(max_length=10, help_text='Enter Phone No')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'phone', 'password1', 'password2')


class ProfileForm(UserCreationForm):
    address = forms.CharField(max_length=50, required=True)
    phone = forms.IntegerField(required=True)

    class Meta:
        model = Profile
        fields = ('address', 'phone')
