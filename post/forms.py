from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import manualform

class Loginform(forms.ModelForm):
    class Meta:
        model=manualform
        fields="__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder':'Username',
                'class': 'bg-transparent my-4 flex justify-center text-2xl mx-auto border-b-2 focus:bg-transparent focus:border-b-2 focus:outline-none focus:border-gray-700  form-control',
                'autocomplete':'off'
                }),
            'password': forms.PasswordInput(attrs={
                'placeholder':'Password' ,
                'class': 'bg-transparent my-2 flex justify-center text-2xl mx-auto border-b-2 focus:bg-transparent focus:border-gray-700 focus:outline-none focus:border-gray-700  form-control',
                'autocomplete':'off'
                }),
        }
    

class Registerform(UserCreationForm):
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder":"Email",
            "class":"block mt-5 border-b-2 w-full text-white bg-black focus:outline-none focus:bg-transparent"
        }
    ))
    class Meta:
        model=User
        fields=('username', 'email', 'password1','password2')

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget=forms.TextInput(attrs={
            "placeholder":"Username",
            "class":"block mt-5 border-b-2 w-full text-white bg-black focus:outline-none focus:bg-transparent"
        })
        self.fields['password1'].widget=forms.TextInput(attrs={
            "placeholder":"Password",
            "class":"block mt-5 border-b-2 w-full text-white bg-black focus:outline-none focus:bg-transparent"
            })

        self.fields['password2'].widget=forms.TextInput(attrs={
            "placeholder":"Confirm Password",
            "class":"block mt-5 border-b-2 w-full text-white bg-black focus:outline-none focus:bg-transparent"
        })
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if '@gmail.com' not in email:
            raise forms.ValidationError("enter a valid gmail")
        return email