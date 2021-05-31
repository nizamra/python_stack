from django.db import models
import os
import re

class userManager(models.Manager):
    def isValid(self, formPOST):
        errors={}
        nameRegex = re.compile(r'([a-zA-Z]).{2,22}')
        if not nameRegex.match(formPOST["fname"]):
            errors["name"] = "name should be at least 2 characters"
        if not nameRegex.match(formPOST["lname"]):
            errors["lastName"] = "name should be at least 2 characters"
        if len(formPOST['bday']) < 2:
            errors["bday"] = "birth day should be at least 2 characters"
        
        emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailRegex.match(formPOST['email']):
            errors['email'] = "Invalid email address!!"

        try:
            thisShow=User.objects.get(email=formPOST['email'])
            errors["retitle"] = "this email is already registered"
        except:
            pass

        passwdRegex = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[-!@#$%^&*()+]).{8,12}')
        if not passwdRegex.match(formPOST["password"]):
            errors['pass'] = "Password Must contain at least one number, one uppercase, lowercase letter, and at least 8 characters max 12"
        return errors
    
    def loginValid(self, formPOST):
        errors={}
        if len(formPOST['password']) < 1:
            errors["password"] = "you have to provide a password"
        
        emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailRegex.match(formPOST['email']):
            errors['email'] = "Invalid email address!!"

        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    birthDate = models.DateField(null=True)
    email = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = userManager()

class Thought(models.Model):
    post = models.TextField()
    uploadeBy=models.ForeignKey(User, related_name="createdThoughts", on_delete=models.CASCADE)
    likedBy=models.ManyToManyField(User, related_name="likes")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

def createThought(desc, userId):
    thisUser = User.objects.get(id=userId)
    thisThought=Thought.objects.create(post=desc,uploadeBy=thisUser)
    thisUser.createdThoughts.add(thisThought)
    return thisThought

def likeSomeThought(id, userId):
    thisUser = User.objects.get(id=userId)
    thisThought=Thought.objects.get(id=id)
    thisUser.likes.add(thisThought)
    return thisThought
    
def unlikeSomeThought(id, userId):
    thisUser = User.objects.get(id=userId)
    thisThought=Thought.objects.get(id=id)
    thisUser.likes.remove(thisThought)
    return thisThought