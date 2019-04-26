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

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'phone', 'password1', 'password2')


class ProfileForm(UserCreationForm):
    address = forms.CharField(max_length=50, required=True)
    phone = forms.IntegerField(required=True)

    class Meta:
        model = Profile
        fields = ('address', 'phone')


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    address = forms.CharField(max_length=254)
    phone = forms.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        super(UpdateProfile, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email',  'address', 'phone')


