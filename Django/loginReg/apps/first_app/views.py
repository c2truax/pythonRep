from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
	request.session.clear()
	return render(request, 'first_app/index.html')

def create(request):
	errors = User.objects.validation(request.POST)
	if len(errors):
		for keys, value in errors.items():
			messages.error(request, value, extra_tags='reg')

		return redirect('/')
	else:
		hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		print(hash)
		new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hash)
		request.session['user_id'] = new_user.id
		return redirect('/success/')
	return redirect('/')

def read(request):
	error = User.objects.login_validation(request.POST)
	if len(error):
		for keys, value in error.items():
			messages.error(request, value, extra_tags='login')

		return redirect('/')
	else:
		request.session['user_id'] = User.objects.get(email = request.POST['username']).id
		return redirect('/success/')



def success(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context= {
	'user': User.objects.get(id = request.session['user_id'])
	}
	return render(request, 'first_app/success.html', context)
