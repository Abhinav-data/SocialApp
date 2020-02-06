from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,UserProfileForm,UserProfileUpdateForm
from Post.models import UserPOST
from .models import UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from Friend.models import Friend
from Post.forms import UserFormModelPost

def userAccountPage(request,user):
	qsData1=UserProfile.objects.get(user__username=user)
	qsData=User.objects.get(username=user)
	qs=UserPOST.objects.filter(user__username=user)[::-1]
	context={'qsD':qsData,'qsD1':qsData1,"querySet":qs}
	return render(request,'userAccountPage.html',context)

def userAccountPageUpdate(request,user):
	obj=get_object_or_404(UserProfile,user__username=user)
	if(request.method=="POST"):
		form=UserProfileUpdateForm(request.POST or None, request.FILES or None ,instance=obj)
		if(form.is_valid()):
			form.save()
		return redirect("/")
	else:
		form=UserProfileUpdateForm(instance=obj)
		context={'form':form}
		return render(request,"userAccountPageEdit.html",context)



def changeFriends(request,user,verb):
	new_friend=User.objects.get(username=user)
	if(verb=="add"):
		Friend.make_friend(request.user, new_friend)
	elif verb=="remove":
		Friend.lose_friend(request.user, new_friend)

	return redirect('home')




