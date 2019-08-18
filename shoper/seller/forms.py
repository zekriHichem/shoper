from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class ShopeForm(forms.ModelForm):
    class Meta:
        model=Shope
        fields = ("address","wilaya","type_shope","logo","bill","num_phone",)
        exclude = ("user","date_creation",)
        widgets = {
            'address': forms.TextInput(attrs={
                'type': 'text',
            }),
            'type_shope': forms.Select(choices=TYPE_SHOPE),
            'wilaya': forms.Select(choices=WILLAYA),

            'num_phone': forms.TextInput(attrs={
                'type': 'text',

            }),
            'logo': forms.FileInput(attrs={
                'type': 'file',

            }),
            'bill': forms.FileInput(attrs={
                'type': 'file',

            }),

        }


class signupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('first_name','last_name','username','email','password1','password2')

        labels={
            'username': 'username',
            'email' : 'email',
            'password1':'password',
            'password2': 'confirm password',
        }
        widgets = {
            'first_name':forms.TextInput(attrs={
                'type': 'text',
                'name': 'first_name',

            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'name': 'last_name',

            }),
            'username': forms.TextInput(attrs={
                'type': 'text',
                'name': 'name',

            }),

            'email': forms.EmailInput(attrs={
                'type': 'email',
                'name': 'email',
            }),
            'password1': forms.PasswordInput(attrs={
                'type': 'password',
                'name': 'psw',
            }),
            'password2': forms.PasswordInput(attrs={
                'type': 'password',
                'name': 'psw',

            }),

        }

    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'name': 'psw', 'placeholder': 'Votre Mot de passe'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'name': 'psw', 'placeholder': 'Confirmer votre Mot de passe'})