from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,UserProfileForm


from django.contrib.auth import authenticate,login,logout

def accountPage(request):
	if request.user.is_authenticated:
		username=request.user.username
	else:
		return redirect('register')
	context={'username':username}
	return render(request,'accountPage.html',context)

def loginPage(request):
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
	if request.method=="POST":
		form=CreateUserForm(request.POST)
		profile_form=UserProfileForm(request.POST, request.FILES)
		print(form.is_valid(),profile_form.is_valid())		
		if(form.is_valid() and profile_form.is_valid()):
			user=form.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			profile.save()

			# username=request.POST.get('username')
			# password=request.POST.get('password')

			# user=authenticate(request,username=username,password=password)
			# if user is not None:
			# 	login(request,user)
			return redirect('login')
	else:
		form=CreateUserForm()
		profile_form=UserProfileForm()
		
	context={"form":form,'profile_form':profile_form}
	return render(request,"registerPage.html",context)

def logoutUser(request):
	logout(request)
	return redirect('login')