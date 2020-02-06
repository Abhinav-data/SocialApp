from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('<slug:slug>', views.PostId,name='postId'),
path('<slug:slug>/delete', views.PostIdDelete,name='PostIdDelete'),
path('<slug:slug>/update', views.PostIdUpdate,name='PostIdUpdate'),
]