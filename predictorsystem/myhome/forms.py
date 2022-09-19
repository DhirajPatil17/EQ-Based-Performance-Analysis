from pyexpat import model

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms import CharField
from django import forms
from matplotlib import widgets

from myhome.models import visualize


class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
   
   
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            # 'password':forms.PasswordInput(attrs={'class':'form-control'})

        }

class Updationform(forms.ModelForm):
    class Meta:
        model=visualize
        fields=['Name','Behavioral','Attendence','Marks']
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Behavioral':forms.NumberInput(attrs={'class':'form-control'}),
            'Attendence':forms.NumberInput(attrs={'class':'form-control'}),
            'Marks':forms.NumberInput(attrs={'class':'form-control'})

        }