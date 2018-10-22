from django.shortcuts import render, redirect
from django.contrib import messages
from ipware import get_client_ip
from .models import User, Category, Job
from .exceptions import *
import bcrypt

def index(request):
	return render(request, 'first_app/index.html')

def create(request):
	if request.method == "POST":
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
			return redirect('/dashboard/')
	else:
		return redirect('/')
	

def read(request):
	error = User.objects.login_validation(request.POST)
	if len(error):
		for keys, value in error.items():
			messages.error(request, value, extra_tags='login')

		return redirect('/')
	else:
		request.session['user_id'] = User.objects.get(email = request.POST['username']).id
		return redirect('/dashboard/')

def logout(request):
	request.session.clear()
	return redirect('/')

def dashboard(request):
	if 'user_id' not in request.session:
		return redirect('/')
	display = {"view" : "d-none"}
	context= {
	'user': User.objects.get(id = request.session['user_id']),
	'alljobs': Job.objects.exclude(users = request.session['user_id']),
	'myjobs': Job.objects.filter(users=request.session['user_id']),
	'display': display
	}
	print()
	return render(request, 'first_app/dashboard.html', context)

def new(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context= {
	'user': User.objects.get(id = request.session['user_id']),
	'categories' : Category.objects.exclude(cat_type = "pet care"),
	}
	return render(request, 'first_app/newjob.html', context)

def createjob(request):
	if request.method == "POST":
		errors = Job.objects.validation(request.POST)
		categories = Category.objects.all()
		breakout = BreakoutException
		try:
			if len(request.POST['othercat']):
				for category in categories:
					if request.POST['othercat'] == category.cat_type:
						errors['category'] = 'Category already available please select it from a radio button above.'
						raise breakout
				category = Category.objects.create(cat_type = request.POST['othercat'])
			elif len(request.POST['category']):
				category = Category.objects.get(cat_type = request.POST['category'])
			else:
				errors['category'] = 'Category needs to be provided.'
		except breakout:
			pass

		if len(errors):
			for keys, value in errors.items():
				messages.error(request, value)

			return redirect('/jobs/new/')
		else:
			new_job = Job.objects.create(title = request.POST['title'], desc = request.POST['desc'], location = request.POST['location'], creator = User.objects.get(id = request.session['user_id']), category = category)
			new_job.users.add(User.objects.get(id=request.session['user_id'])) 
			return redirect('/dashboard/')
	else:
		return redirect('/')

def edit(request,id):
	if 'user_id' not in request.session:
		return redirect('/')
	context= {
	'user': User.objects.get(id = request.session['user_id']),
	'job': Job.objects.get(id=id),
	'categories': Category.objects.all().exclude(id = Job.objects.get(id=id).category.id)
	}
	return render(request, 'first_app/editjob.html', context)

def editjob(request,id):
	if 'user_id' not in request.session:
		return redirect('/')
	if request.method == "POST":
		errors = Job.objects.validation(request.POST)
		categories = Category.objects.all()
		breakout = BreakoutException
		try:
			if len(request.POST['newcat']):
				for category in categories:
					if request.POST['newcat'] == category.cat_type:
						errors['category'] = 'Category already available please select it from the drop down list.'
						raise breakout
				category = Category.objects.create(cat_type = request.POST['newcat'])
			elif len(request.POST['category']):
				category = Category.objects.get(cat_type = request.POST['category'])
			else:
				errors['category'] = 'Category needs to be provided.'
		except breakout:
			pass
		if len(errors):
			for keys, value in errors.items():
				messages.error(request, value)

			return redirect('/jobs/edit/'+id)
		else:
			update_job = Job.objects.get(id=id)
			update_job.title = request.POST['title']
			update_job.desc = request.POST['desc']
			update_job.location = request.POST['location']
			update_job.category = category
			update_job.save()
			return redirect('/dashboard/')
	else:
		return redirect('/')
	return redirect('/dashboard/')

def viewjob(request,id):
	if 'user_id' not in request.session:
		return redirect('/')
	doers = Job.objects.get(id=id).users.all()
	display = {"view" : "d-none"}
	for doer in doers:
		if doer.id == request.session['user_id']:
			display['doer'] = 1
		else:
			display['doer'] = 0
	print(display)
	context= {
	'user': User.objects.get(id = request.session['user_id']),
	'job': Job.objects.get(id=id),
	'doers': doers, 
	'display': display,
	}
	return render(request, 'first_app/viewjob.html', context)

def addjob(request,id):
	if 'user_id' not in request.session:
		return redirect('/')
	job = Job.objects.get(id=id)
	job.users.add(User.objects.get(id=request.session['user_id']))

	return redirect('/dashboard/')

def deletejob(request,id):
	if 'user_id' not in request.session:
		return redirect('/')
	try:
		job = Job.objects.get(id=id)
		if request.session.user_id != job.creator.id:
			if 'warn' not in request.session:
				request.session['warn'] = True 
				return redirect('/danger/')
			else:
				return redirect('/logout/')
		job.delete()
	except:
		if 'warn' not in request.session:
			request.session['warn'] = True 
			return redirect('/danger/')
		else:
			return redirect('/logout/')

	return redirect('/dashboard/')

def donejob(request,id):
	if 'user_id' not in request.session:
		return redirect('/')
	try:
		job = Job.objects.get(id=id)
		doers = Job.objects.get(id=id).users.all()
		for doer in doers:
			if doer.id == request.session['user_id']:
				job.delete()
				return redirect('/dashboard/')
		if 'warn' not in request.session:
			request.session['warn'] = True 
			return redirect('/danger/')
		else:
			return redirect('/logout/')
	except:
		if 'warn' not in request.session:
			request.session['warn'] = True 
			return redirect('/danger/')
		else:
			return redirect('/logout/')

	

def removejob(request,id):
	if 'user_id' not in request.session:
		return redirect('/')
	job = Job.objects.get(id=id)
	job.users.remove(User.objects.get(id=request.session['user_id']))

	return redirect('/dashboard/')

def danger(request):
	ip, is_routable = get_client_ip(request)
	context = {
	'ipaddress' : ip
	}
	return render(request, 'first_app/danger.html', context)