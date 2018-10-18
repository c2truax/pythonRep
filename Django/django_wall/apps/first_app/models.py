from django.db import models
from django.core.validators import validate_email, ValidationError
import bcrypt


class UserManager(models.Manager):
    def validation(self, postdata):
        errors = {}
        if len(postdata['first_name']) < 2:
            errors['first_name'] = 'First name needs to be at least 2 characters.'
        if len(postdata['last_name']) < 2:
            errors['last_name'] = 'Last name needs to be at least 2 characters.'
        if len(postdata['password']) < 8:
            errors['password'] = 'password needs to be at least 8 characters.'
        try:
            validate_email(postdata['email'])
        except ValidationError as e:
            errors['email'] = 'invalid email format.'
        if postdata['password'] != postdata['passconfirm']:
            errors['password_confirm'] = 'passwords must match.'
        try:
            User.objects.get(email = postdata['email'])
            errors['email_taken'] = 'email has already been registered'
        except:
            print('success')


        return errors
    def login_validation(self,postdata):
        errors={}
        try:
            user = User.objects.get(email = postdata['username'])
            print('email')
            bcrypt.checkpw(postdata['pw'].encode(), user.password.encode())
            print('password')
        except Exception as e:
            errors['login'] = 'invalid login'
            print(e)
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Message(models.Model):
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='messages')

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='user_comments')
    parentMessage = models.ForeignKey(Message, related_name='comments')
