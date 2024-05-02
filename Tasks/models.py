from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

class Task(models.Model):
    author = models.ForeignKey(user,on_delete = models.CASCADE)
    title = models.CharField(max_length=150,null=True,blank=True)
    description = models.TextField()
    deadline = models.DateField()
    priority = models.TextField()
    pending = 'P'
    In_progress ='I'
    complete = 'C'
    options = ((pending,'pending'),(In_progress,'in progress'),(complete,'complete'))
    status = models.CharField(max_length = 1,default =pending,choices = options)
    date_created = models.DateField(auto_now_add = True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    collaborative_users = models.ForeignKey(user,on_delete = models.SET_NULL,null = True ,blank  =True)