from django.db import models
import re

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        # emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not emailRegex.match(postData['email']):
        #     errors['email'] = "Invalid email address!!"
        if len(postData['titleField']) < 2 :
            errors["title"] = "title is too short, must be longer than 2"
        if len(postData['networkField']) < 3 :
            errors["network"] = "network is shorter than 3 wich is not accepted"
        if len(postData['descriptionField']) < 10 :
            errors["description"] = "description should be at least 10 characters"
        if len(postData['releaseDateField']) < 2 :
            errors["releaseDate"] = "releaseDate is short"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.DateField()
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects=ShowManager()