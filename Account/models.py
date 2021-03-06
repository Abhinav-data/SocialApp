from django.db import models
from django import forms
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	profilePic=models.ImageField(upload_to='profile_image/', default='profile_image/default.png',blank=True)
	
	def __str__(self):
		return self.user.username


