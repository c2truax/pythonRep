from django.db import models
from django.core.validators import validate_email, ValidationError
import bcrypt
import django.utils.timezone

class UserManager(models.Manager):
	def validation(self, postdata):
		errors = {}

		if len(postdata['alias']) < 2:
			errors['alias'] = 'Alias needs to be at least 2 characters.'
		if len(postdata['name']) < 2:
			errors['name'] = 'Name needs to be at least 2 characters.'
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
			bcrypt.checkpw(postdata['pw'].encode(), user.password.encode())
			print('password')

		except Exception as e:
			errors['login'] = 'invalid login'
			print(e)
		return errors

class User(models.Model):
	alias = models.CharField(max_length = 255)
	name = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Author(models.Model):
	name = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
	title = models.CharField(max_length = 255)
	author = models.ForeignKey(Author, related_name="books", default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
	review = models.TextField(max_length=1000)
	rating = models.SmallIntegerField()
	user = models.ForeignKey(User,related_name="user_reviews")
	book = models.ForeignKey(Book, related_name="book_reviews")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)




