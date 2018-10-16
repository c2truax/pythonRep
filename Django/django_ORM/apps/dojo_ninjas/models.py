from __future__ import unicode_literals
from django.db import models
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.name}"
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name = "ninjas")
    def __str__(self):
        return f"{self.first_name}"
