from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,UserProfileForm
from Post.models import UserPOST
from .models import UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from Friend.models import Friend



def accountPage(request):
	if request.user.is_authenticated:
		username=request.user
		qs=UserPOST.objects.filter(user__username=request.user)[::-1]
	else:
		qs=""
		return redirect('login')
	context={'username':username,"querySet":qs}
	return render(request,'accountPage.html',context)

def userAccountPage(request,user):
	qsData1=UserProfile.objects.get(user__username=user)
	qsData=User.objects.get(username=user)
	print(qsData)
	qs=UserPOST.objects.filter(user__username=user)[::-1]
	context={'qsD':qsData,'qsD1':qsData1,"querySet":qs}
	return render(request,'userAccountPage.html',context)

def changeFriends(request,user,verb):
	new_friend=User.objects.get(username=user)
	if(verb=="add"):
		Friend.make_friend(request.user, new_friend)
	elif verb=="remove":
		Friend.lose_friend(request.user, new_friend)

	return redirect('home')





