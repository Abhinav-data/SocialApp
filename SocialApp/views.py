from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from Post.models import UserPOST
from Post.forms import UserFormModelPost

@login_required(login_url='/account')
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
