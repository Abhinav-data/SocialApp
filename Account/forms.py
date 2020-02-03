from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile
from Post.models import UserPOST

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(max_length=30,required=True)
	last_name = forms.CharField(max_length=30)

	class Meta:
		model=User
		fields=['username','first_name','last_name','email','password1','password2']

	def save(self, commit=True):
	    user = super().save(commit=False)
	    user.email = self.cleaned_data['email']
	    user.first_name = self.cleaned_data['first_name']
	    user.last_name = self.cleaned_data['last_name']
	    if commit:
	        user.save()
	    return user

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('profilePic',)
