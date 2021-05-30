# from django.db.models.aggregates import Max
from django.db import models
import re


class postManager(models.Manager):
    
    def postIsValid(self, text):
    
        errors={}
        postRegex = re.compile(r'([a-zA-Z]).{8,80}')
        if not postRegex.match(text):
            errors["post"] = "post should be 8-80 chars"
        return errors


class commentManager(models.Manager):

    def commentIsValid(self, formPOST):
    
        errors={}
        nameRegex = re.compile(r'([a-zA-Z]).{5,72}')
        if not nameRegex.match(formPOST["fname"]):
            errors["name"] = "name should be 5-72 chars"
        return errors



class Post(models.Model):

    postTxt = models.TextField()
    createdBy = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = postManager()


class Comment(models.Model):

    commentTxt = models.TextField()
    createdBy = models.ManyToManyField(User, related_name="comments")
    onPost = models.ManyToManyField(Post, related_name="comments")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = commentManager()