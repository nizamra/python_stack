from django.db import models
import re
from time import localtime, strftime

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        try:
            thisShow=Show.objects.get(title=postData['titleField'])
            errors["retitle"] = "this title is repeated"
        except:
            pass

        # emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not emailRegex.match(postData['email']):
        #     errors['email'] = "Invalid email address!!"

        if len(postData['titleField']) < 2 :
            errors["title"] = "title is too short, must be longer than 2"
        if len(postData['networkField']) < 3 :
            errors["network"] = "network is shorter than 3 wich is not accepted"
        if not (len(postData['descriptionField']) == 0 or  len(postData['descriptionField']) > 10) :
            errors["description"] = "description should be at least 10 characters"

        todayTime= strftime("%Y-%m-%d", localtime())
        postTime = postData['releaseDateField']
        todayTimeList = todayTime.split("-")
        postTimeList = postTime.split("-")
        if (todayTimeList[0] <= postTimeList[0]):
            if  (todayTimeList[1] <= postTimeList[1]):
                if (todayTimeList[2] < postTimeList[2]):
                    errors["releaseDate"] = "releaseDate is in the future"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.DateField()
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects=ShowManager()