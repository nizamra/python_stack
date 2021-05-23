from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(max_length=255, null=True)

class Ninja(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dojoId = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)