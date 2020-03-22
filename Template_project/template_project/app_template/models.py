from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length = 128)


