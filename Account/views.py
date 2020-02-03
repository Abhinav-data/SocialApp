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



def accountPage(request):
	if request.user.is_authenticated:
		username=request.user
		qs=UserPOST.objects.filter(user__username=request.user)
	else:
		qs=""
		return redirect('login')
	context={'username':username,"querySet":qs}
	return render(request,'accountPage.html',context)

def userAccountPage(request,user):
	if request.user.is_authenticated:
		qsData1=UserProfile.objects.get(user__username=user)
		qsData=User.objects.get(username=user)
		print(qsData)
		qs=UserPOST.objects.filter(user__username=user)
	else:
		qs=""
		return redirect('login')
	context={'qsD':qsData,'qsD1':qsData1,"querySet":qs}
	return render(request,'userAccountPage.html',context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('accountPage')
	else:
		if request.method=="POST":
			username=request.POST.get('username')
			password=request.POST.get('password')

			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('accountPage')
		context={}
		return render(request,"loginPage.html",context)


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('accountPage')
	else:
		if request.method=="POST":
			form=CreateUserForm(request.POST)
			profile_form=UserProfileForm(request.POST, request.FILES)
			if(form.is_valid() and profile_form.is_valid()):
				user=form.save()
				profile=profile_form.save(commit=False)
				profile.user=user
				profile.save()

				return redirect('login')
		else:
			form=CreateUserForm()
			profile_form=UserProfileForm()

		context={"form":form,'profile_form':profile_form}
		return render(request,"registerPage.html",context)

def logoutUser(request):
	logout(request)
	return redirect('login')
