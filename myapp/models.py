from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    
    source = models.CharField(max_length = 500, blank = True)
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)