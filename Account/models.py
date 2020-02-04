from django.db import models
from django import forms
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	profilePic=models.ImageField(upload_to='profile_image/', default='profile_image/default.png',blank=True)
	
	def __str__(self):
		return self.user.username

# class Friend(models.Model):
#     users = models.ManyToManyField(User)
#     current_user = models.ForeignKey(User, related_name="owner", null=True,on_delete=models.CASCADE)

#     @classmethod
#     def make_friend(cls, current_user, new_friend):
#         friend, created = cls.objects.get_or_create(
#             current_user = current_user
#         )
#         friend.users.add(new_friend)

#     @classmethod
#     def remove_friend(cls, current_user, new_friend):
#         friend, created = cls.objects.get_or_create(
#             current_user = current_user
#         )
#         friend.users.remove(new_friend)

#     def __str__(self):
#         return str(self.current_user)
