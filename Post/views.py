from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from Post.forms import UserFormModelPost
from django.contrib.auth.models import User
from Account.forms import CreateUserForm,UserProfileForm
from .models import UserPOST

def PostId(request,slug):
	post=UserPOST.objects.get(slug=slug)
	context={"post":post}
	return render(request,"idPost.html",context)

def PostIdDelete(request,slug):
	post=UserPOST.objects.get(slug=slug)
	post.delete()
	return redirect('/')

def PostIdUpdate(request,slug):
	obj=get_object_or_404(UserPOST,slug=slug)
	form=UserFormModelPost(request.POST or None, request.FILES or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect("/")
	obj.delete()
	context={'form':form}
	return render(request,"idPostUpdate.html",context)


