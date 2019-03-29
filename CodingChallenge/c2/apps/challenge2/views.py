from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.db import IntegrityError

from .models import User

import bcrypt

def index(request):
    return render(request, 'challenge2/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return HttpResponseRedirect(reverse('c2:index'))

    try:
        hashpwd = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST.get('name'),
                                   email=request.POST.get('email').lower(),
                                   password=hashpwd)
    except IntegrityError:
        messages.error(request, "This email is already registered!", extra_tags='email')
        return HttpResponseRedirect(reverse('c2:index'))
    except Exception:
        messages.error(request, "Unable to process your request!", extra_tags='email')
        return HttpResponseRedirect(reverse('c2:index'))

    if user:
        set_session(request, user)
        return HttpResponseRedirect(reverse('c2:dashboard'))
    else:
        return HttpResponseRedirect(reverse('c2:index'))

def login(request):
    user = get_user_email(request.POST.get('email'))
    if user:
        if bcrypt.checkpw(request.POST.get('password').encode(), user.password):
            set_session(request, user)
            return HttpResponseRedirect(reverse('c2:dashboard'))
    messages.error(request, "Bad Credentials!", extra_tags='login')
    return HttpResponseRedirect(reverse('c2:index'))

def dashboard(request):
    if not logged_in(request):
        messages.error(request, "Please log in", extra_tags='login')
        return HttpResponseRedirect(reverse('c2:index'))
    return render(request, 'challenge2/dashboard.html',)

def edit(request, uid):
    if not logged_in(request):
        messages.error(request, "Please log in", extra_tags='login')
        return HttpResponseRedirect(reverse('c2:index'))
    return render(request, 'challenge2/edit.html', {'uid': uid})

def update(request, uid):
    try:
        user = User.objects.get(id=uid)
        name = request.POST['name']
        email = request.POST['email']
        if user.email != request.POST['email']:
            email = user.email

        user.name = name
        user.email = email
        user.save()

        request.session['name'] = user.name
        request.session['email'] = user.email

        return HttpResponseRedirect(reverse('c2:dashboard'))
    except Exception:
        messages.error(request, "Update failed!", extra_tags='edit')
        return HttpResponseRedirect(reverse('c2:edit', kwargs={'uid': uid}))

def destroy(request, uid):
    try:
        user = User.objects.get(id=uid)
        user.delete()
        request.session.flush()
        return HttpResponseRedirect(reverse('c2:index'))
    except Exception:
        messages.error(request, "Delete error!", extra_tags='login')
        return HttpResponseRedirect(reverse('c2:index'))

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('c2:index'))

def logged_in(request):
    return request.session.get('user_id')

def get_user_email(email):
    try:
        return User.objects.get(email=email.lower())
    except Exception:
        return False

def set_session(request, user):
    request.session['name'] = user.name
    request.session['user_id'] = user.id
    request.session['email'] = user.email
    request.session['password'] = user.password.decode()
