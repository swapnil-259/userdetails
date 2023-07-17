from django.db import models

class Register_user(models.Model):
    First_Name = models.CharField(max_length=50, blank=False)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50, blank= False, unique=True)
    Gender_Choices = (
          ('M','Male'),
         ('F','Female'),
         ('O','Others'),
     )
    Gender = models.CharField(max_length=1, choices=Gender_Choices, blank=False)
    Address = models.CharField(max_length=150, blank= False)
    Stay_Choices = (
         ('H','Hostel'),
         ('D','Day_Scholar'),
     )
    Stay = models.CharField(max_length=1, choices=Stay_Choices, blank= False)
    Password = models.CharField(max_length=200, blank=False, default="")
    Status = models.CharField(max_length=2, default="", blank=False)

class todo(models.Model):

    Identity = models.ForeignKey(Register_user, on_delete=models.CASCADE)
    Entryno = models.AutoField(primary_key=True)
    Task = models.CharField(max_length=255, null=True)
    taskno = models.CharField(default=0,max_length=1)
    Tasktime = models.DateTimeField(auto_now_add=True, blank=True)
    UpdateTask = models.BooleanField(default=False)
    Updatetime = models.DateTimeField(blank=True,null=True)
    DeleteTask = models.BooleanField(default=False)
    Deletetime = models.DateTimeField(blank=True,null=True)
    CompleteTask = models.BooleanField(default=False)
    Completetime = models.DateTimeField(blank=True,null=True)








   
    


    
    
