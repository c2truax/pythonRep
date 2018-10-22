from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Author, Book, Review
import bcrypt

def index(request):
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
		new_user = User.objects.create(alias = request.POST['alias'], name = request.POST['name'], email = request.POST['email'], password = hash)
		request.session['user_id'] = new_user.id
		return redirect('/books/')
	return redirect('/')

def read(request):
	error = User.objects.login_validation(request.POST)
	if len(error):
		for keys, value in error.items():
			messages.error(request, value, extra_tags='login')

		return redirect('/')
	else:
		request.session['user_id'] = User.objects.get(email = request.POST['username']).id
		return redirect('/books/')

def books(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context= {
	'user': User.objects.get(id = request.session['user_id']),
	'reviews': Review.objects.all().order_by('-id')[:3],
	'books': Book.objects.all()
	}
	return render(request, 'first_app/books.html', context)

def view_book(request,id):
	if 'user_id' not in request.session:
		return redirect('/')
	context= {
	'user': User.objects.get(id = request.session['user_id']),
	'reviews': Review.objects.all(),
	'book': Book.objects.get(id = id),
	}

	return render(request, 'first_app/bookview.html', context)

def user_review(request,id):
	if 'user_id' not in request.session:
		return redirect('/')
	context= {
	'user': User.objects.get(id = request.session['user_id']),
	'userview': User.objects.get(id = id),
	'reviews': Review.objects.filter(user=id),
	'count': Review.objects.filter(user=id).count()
	}

	return render(request, 'first_app/user_review.html', context)

def compute_add(request):
	if request.POST['add_author']:
		author = Author.objects.create(name=request.POST['add_author'])
	else:
		author = Author.objects.get(name=request.POST['author_name'])
	Review.objects.create(review=request.POST['review'],rating=request.POST['rating'],user=User.objects.get(id=request.session['user_id']),book=Book.objects.create(title=request.POST['title'],author=author))
	id=str(Book.objects.last().id)
	return redirect('/books/'+id)

def compute_review(request):
	bookinstance = Book.objects.get(id=request.POST['book_id'])
	Review.objects.create(review=request.POST['review'],rating=request.POST['rating'],user=User.objects.get(id=request.session['user_id']),book=bookinstance)
	id=request.POST['book_id']
	return redirect('/books/'+id)

def add(request):
	if 'user_id' not in request.session:
		return redirect('/')
	context= {
	'user': User.objects.get(id = request.session['user_id']),
	'authors': Author.objects.all()
	}
	return render(request, 'first_app/add.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')

def delete(request,id):
	review = Review.objects.get(id=id)
	id = str(review.book.id)
	review.delete()
	return redirect('/books/'+id)
