from django.db import models

# Create your models here.
class Reg(models.Model):
    FirstName= models.CharField(max_length=10)
    LastName=models.CharField(max_length=10)
    UserName=models.CharField(max_length=10,unique=True)
    Password=models.CharField(max_length=18)
    RePassword=models.CharField(max_length=18)
    Email=models.EmailField()
    
    def __str__(self):
        return self.UserName
    

