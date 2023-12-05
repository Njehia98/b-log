from django.db import models
from django.contrib.auth.models import User  # Import the User model for author association
from django.utils import timezone

class Outfit(models.Model):
    category = models.CharField(max_length=200)
    content = models.TextField()
   

    def __str__(self):
        return self.content 

class Cloth (models.Model):
    gender=models.CharField(max_length=200)
    name= models.CharField(max_length=200)
    size= models.IntegerField()
    
    def __str__(self):
        return self.name

class Shoes (models.Model):
    size=models.IntegerField()
    type:models.TextField()
    gender:models.CharField(max_length=200)
    category:models.CharField(max_length=200)

   