"""SocialApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.accountPage,name='accountPage'),
    path('<str:user>', views.userAccountPage,name='useraccountPage'),
    path('<str:user>/update', views.userAccountPageUpdate,name='useraccountPageUpdate'),
    path('<str:user>/<str:verb>', views.changeFriends,name='changeFriends'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
