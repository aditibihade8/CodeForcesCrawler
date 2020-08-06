# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class UserForm(UserCreationForm) :
# 	cf_handle = forms.CharField(help_text = 'Required. Provide valid CodeForces Handle')
# 	class Meta() :
# 		model = User
# 		fields = ('username','password','password2','cf_handle')

from django import forms
#from django.models import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	cf_handle = forms.CharField(help_text = 'Required. Provide valid CodeForces Handle')

	class Meta():
		model = User
		fields = ('username','password1', 'password2', 'cf_handle')
