from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages

from .models import User
import bcrypt

def index(request):
    return render(request, 'challenge1/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return HttpResponseRedirect(reverse('c1:index'))
    else:
        hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'],
                               email=request.POST['email'].lower(),
                               password=hash)

    if user:
        set_session(request, user)
        return HttpResponseRedirect(reverse('c1:dashboard'))
    else:
        return HttpResponseRedirect(reverse('c1:index'))

def login(request):
    user = get_user_email(request.POST['email'])
    if user:
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()) == True:
            set_session(request, user)
            return HttpResponseRedirect(reverse('c1:dashboard'))
    messages.error(request, "Bad Credentials!", extra_tags='login')
    return HttpResponseRedirect(reverse('c1:index'))

def show(request, uid):
    return render(request, 'challenge1/show.html',)

def dashboard(request):
    return render(request, 'challenge1/dashboard.html',)

def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('c1:index'))

def get_user_email(email):
    try:
        return User.objects.get(email=email.lower())
    except Exception:
        return False

def set_session(request, user):
    request.session['name'] = user.name
    request.session['user_id'] = user.id
    request.session['email'] = user.email
