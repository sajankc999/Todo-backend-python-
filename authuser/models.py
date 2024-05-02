from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    first_name=models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150,null=True,blank=True,default='')
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100,unique=True)
    username = models.CharField(max_length=125,null=True,blank =True,default = 'user')

    # objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]

    is_user = models.BooleanField(default=True)
    