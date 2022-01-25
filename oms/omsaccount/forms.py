from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_Profile

class User_Account(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'password1', 'password2']

class Profile_Form(ModelForm):
    class Meta:
        model = User_Profile
        fields = '__all__'