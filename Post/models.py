from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
import string 
import random 

User=settings.AUTH_USER_MODEL

class UserPOST(models.Model):
    user=models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    content=models.TextField(max_length=255, blank=True)
    slug=models.SlugField(max_length=250,null=True,blank=True)
    image=models.ImageField(upload_to='post_image/',blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.user.username)+ ", "+ self.content[:50]+", "+str(self.id)



def slug_generator(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=''.join(random.choices(string.ascii_lowercase + string.digits, k = 7)) 

pre_save.connect(slug_generator,sender=UserPOST)
