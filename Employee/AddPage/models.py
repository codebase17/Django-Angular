from django.db import models

# Create your models here.
class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)   

class UserDetails(models.Model):
    Users = models.ForeignKey(Users, on_delete=models.CASCADE)
    Pincode = models.IntegerField()   
    Status = models.IntegerField()

