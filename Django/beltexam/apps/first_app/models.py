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
			errors['password'] = 'Password needs to be at least 8 characters.'
		try:
			validate_email(postdata['email'])
		except ValidationError as e:
			errors['email'] = 'Invalid email format.'
		if postdata['password'] != postdata['passconfirm']:
			errors['password_confirm'] = 'Passwords must match.'
		
		try:
			User.objects.get(email = postdata['email'])
			errors['email_taken'] = 'Email has already been registered'
		except:
			print('success')

		return errors

	def login_validation(self,postdata):
		errors={}

		try:
			user = User.objects.get(email = postdata['username'])
			print('email')
			
			print('password')

		except Exception as e:
			errors['login'] = 'invalid login'
			print(e)
		if bcrypt.checkpw(postdata['pw'].encode(), user.password.encode()) == False:
			errors['login'] = 'invalid login'
		return errors

class CategoryManager(models.Manager):
	def validation(self, postdata):
		errors = {}
		return errors

class JobManager(models.Manager):
	def validation(self, postdata):
		errors = {}
		if len(postdata['title']) < 3:
			errors['title'] = 'Title needs to be at least 3 characters.'
		if len(postdata['desc']) < 3:
			errors['desc'] = 'Description needs to be at least 3 characters.'
		if len(postdata['location']) < 3:
			errors['location'] = 'Location needs to be at least 3 characters.'
		
		return errors


class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Category(models.Model):
	cat_type = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CategoryManager()

class Job(models.Model):
	title = models.CharField(max_length = 255)
	desc = models.TextField(max_length = 1000)
	location = models.CharField(max_length = 255)
	creator = models.ForeignKey(User, related_name="myjobs")
	users = models.ManyToManyField(User, related_name="jobs")
	category = models.ForeignKey(Category, related_name="jobs")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = JobManager()


