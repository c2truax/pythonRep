from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Name should be more than 5 characters"
        if len(postData['description']) < 15:
            errors["description"] = "Description should be more than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
    def __str__(self):
        return f'{self.name}'
