from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)  #on_delete=models.CASCADE field is required!

    #aditional 
    portfolio_site  = models.URLField(blank=True)


    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username # username is a default attribute of oneToOneField()




