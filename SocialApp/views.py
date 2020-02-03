from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from Post.models import UserPOST
from Post.forms import UserFormModelPost

@login_required(login_url='account')
def home(request):
	form=UserFormModelPost(request.POST or None, request.FILES or None)
	if(form.is_valid()):
		obj=form.save(commit=False)
		obj.user=request.user
		obj.save()
		form=UserFormModelPost()
	qs=UserPOST.objects.all()
	context={"querySet":qs,"form":form}
	return render(request,"home.html",context)

def UserAccount(request):
	if request.user.is_authenticated:
		username=request.user
		qs=UserPOST.objects.filter(user__username=request.user)
	else:
		qs=""
		return redirect('/login')
	context={'username':username,"querySet":qs}
	return render(request,'accountPage.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')
