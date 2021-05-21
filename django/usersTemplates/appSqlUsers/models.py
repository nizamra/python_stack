from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.TextField()
    age= models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)