from django.db import models
import re

class userManager(models.Manager):
    def isValid(self, formPOST):
        errors={}
        if len(formPOST['fname']) < 2:
            errors["name"] = "name should be at least 2 characters"
        if len(formPOST['lname']) < 2:
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

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    birthDate = models.DateField(null=True)
    email = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = userManager()