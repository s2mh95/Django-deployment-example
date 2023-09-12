from django import forms
from django.contrib.auth.models import User
from pssapp.models import UserPorfileInfo

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
class UserPorfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserPorfileInfo
        fields = ('protfolio_site', 'profile_pic')
        