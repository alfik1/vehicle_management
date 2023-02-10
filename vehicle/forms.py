
from django import forms
from vehicle.models import Vehicle,Users
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-dark',"placeholder":"enter your password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-success', 'placeholder': 'Enter your password again'}))

    class Meta:
        model=Users
        fields=['username', 'email','options']

        widgets={
            "username":forms.TextInput(attrs={'class': 'form-control border border-dark', 'placecholder': 'enter your username'}),
            "options":forms.Select(attrs={'class': 'form-control border border-success'}),
            "email":forms.EmailInput(attrs={'class':'form-control border border-dark','placeholder': 'Enter your email'}),
            
        }
class LoginForm(forms.Form):
    username =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border border-dark',"placeholder":"enter your password"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-dark',"placeholder":"enter your password"}))


class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=['vehicle_number','vehicle_type','vehicle_model','vehicle_description']

        widgets={
            "vehicle_number":forms.TextInput(attrs={'class':'form-control border border-dark','placeholder':'Enter Vehicle number'}),
            "vehicle_type":forms.Select(attrs={'class': 'form-control border border-success'}),
            "vehicle_model":forms.TextInput(attrs={'class':'form-control border border-dark','placeholder':'Enter Vehicle model'}),
            'vehicle_description':forms.TextInput(attrs={'class':'form-control border border-success '})
        }