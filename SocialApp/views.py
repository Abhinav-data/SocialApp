from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

@login_required(login_url='/account')
def home(request):
	context={}
	return render(request,"index.html",context)