from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email, ValidationError
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def check_pwd_confirm(self, postData, errors):
        if len(postData['password']) < 1:
            errors["password"] = "Password cannot be empty"
        elif len(postData['password']) < 6:
            errors["password"] = "Password must be more than 6 characters"

        if postData['password'] != postData['password_confirmation']:
            errors["pwd_confirm"] = "Passwords don't match! Please enter again"

    def check_name(self, postData, errors):
        if len(postData['name']) < 1:
            errors["name"] = "First Name cannot be empty"
        elif len(postData['name']) < 2:
            errors["name"] = "First Name should be atleast 2 characters"
        elif not postData['name'].isalpha():
            errors["name"] = "First Name should contain only letters"

    def check_email(self, postData, errors):
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Not a Valid Email"

    def basic_validator(self, postData):
        errors = {}

        self.check_name(postData, errors)
        self.check_email(postData, errors)
        self.check_pwd_confirm(postData, errors)

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return 'id={}, name={}, email={}, password={}'. \
            format(self.id, self.name, self.email, self.password)
