from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL

class UserPOST(models.Model):
    user=models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    content=models.TextField(max_length=255, blank=True)
    image=models.ImageField(upload_to='post_image/',blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.user.username)+ ", "+ self.content[:50]


