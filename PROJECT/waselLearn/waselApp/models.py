from django.db.models.fields.files import ImageField
from time import localtime, strftime
from ..loginAuth.models import User
from django.db import models
import os
import re

class SugestionManager(models.Manager):
    def sugestionIsValid(self, formPOST):

        """
        fullName: name of user who made the sugestion
        email: must be valid format
        description: at least three words
        """
        errors={}
        emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailRegex.match(formPOST['email']):
            errors['email'] = "Invalid email address!!"
        nameRegex = re.compile(r'([a-zA-Z]).{3,45}')
        if not nameRegex.match(formPOST["fullName"]):
            errors["name"] = "name should be at least 3 characters, can't contain numbers"
        descRegex = re.compile(r'([a-zA-Z0-9]).{15,}')
        if not descRegex.match(formPOST["description"]):
            errors["description"] = "description should be at least 15 characters"
        return errors


class SessionManager(models.Manager):
    def sessionIsValid(self, formPOST):
        
        """

        """
        errors={}
        return errors


class dayTimeSlotManager(models.Manager):
    def dayTimeSlotIsValid(self, formPOST):
        
        """

        """
        errors={}
        return errors        




class Sugestion(models.Model):

    """
    title: the header of the comment
    fullNamename of the commenter
    email: provide email to get back to
    description: the body of the sugestion itself
    ubdatedBy: if theres a user in the session populate this field
    createdAt: date and time this Sugestion was created
    updatedAt: last time an update was done on this Sugestion
    """
    title = models.CharField(max_length=55)
    fullName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    description = models.TextField()
    ubdatedBy=models.ForeignKey(User, related_name="sugestied", null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = SugestionManager()


class Session(models.Model):

    """
    title: title of the session can be empty
    bookedBy: the user who booked the session
    bookedWith: the teacher for this session
    createdAt: date and time this session was created
    updatedAt: last time an update was done on this session
    """
    title = models.CharField(max_length=55, null=True)
    bookedBy=models.ForeignKey(User, related_name="booked", null=True)
    bookedWith=models.ForeignKey(User, related_name="bookedAt", null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = SessionManager()


class dayTimeSlot(models.Model):

    """
    name: name of time slot(first, second, ..., twelveth)
    timeslot: time of slot(8-9,9-10, ...,16-17)
    """
    name = models.CharField(max_length=20)

    timeslot = models.TimeField()
    objects = dayTimeSlotManager()