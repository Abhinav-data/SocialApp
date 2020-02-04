from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from Post.models import UserPOST
from Post.forms import UserFormModelPost
from django.contrib.auth.models import User
from Account.forms import CreateUserForm,UserProfileForm
from Post.models import UserPOST
from Account.models import UserProfile
from Friend.models import Friend

@login_required(login_url='login')
def home(request):
	form=UserFormModelPost(request.POST or None, request.FILES or None)
	if(form.is_valid()):
		obj=form.save(commit=False)
		obj.user=request.user
		obj.save()
		form=UserFormModelPost()

	users = User.objects.exclude(id=request.user.id)
	qs=UserPOST.objects.all()[::-1]
	friend=Friend.objects.get(current_user=request.user)
	friends=friend.users.all()

	context={"querySet":qs,"form":form,"users":users,'friends':friends}
	return render(request,"home.html",context)

def UserAccount(request):
	if request.user.is_authenticated:
		username=request.user
		qs=UserPOST.objects.filter(user__username=request.user)
	else:
		qs=""
		return redirect('login')
	context={'username':username,"querySet":qs}
	return render(request,'accountPage.html',context)

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


# @login_required
# def add_or_remove_friends(request, username, verb):
#     n_f = get_object_or_404(User, username=username)
#     owner = request.user.userprofile
#     new_friend = UserProfile.objects.get(user=n_f)

#     if verb == "add":
#         new_friend.followers.add(owner)
#         Friend.make_friend(owner, new_friend)
#     else:
#         new_friend.followers.remove(owner)
#         Friend.remove_friend(owner, new_friend)

#     return redirect('account')
