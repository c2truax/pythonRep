from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User, Message, Comment
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
    'user': User.objects.get(id=request.session['user_id']),
    'posts': Message.objects.all().order_by('-created_at'),
    'comments': Comment.objects.all()
    }
    return render(request, 'first_app/success.html', context)

def send(request):
    Message.objects.create(message=request.POST['message'], user=User.objects.get(id=request.session['user_id']))
    return redirect('/success/')

def addcomment(request):
    Comment.objects.create(comment=request.POST['comment'], user=User.objects.get(id=request.session['user_id']), parentMessage = Message.objects.get(id=request.POST['message_id']))
    return redirect('/success/')


def logout(request):
    request.session.clear()
    return redirect('/')
