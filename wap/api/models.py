from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=233)
    email = models.CharField(max_length=23)
    password  = models.CharField(max_length= 14)
    
    
    def __str__(self):
        return self.name
    
    
class Pet(models.Model):
    title = models.CharField(max_length=234)
    description = models.CharField(max_length=433) 
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    
    
    def __str__(self):
        return self.title  
