from django.db import models

class book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class author(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    booksconnection = models.ManyToManyField(book, related_name="authors")