from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

#This class is basicly creates form with User built-in model
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

#This class is basicly creates form with UserProfileInfo model that we created
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
