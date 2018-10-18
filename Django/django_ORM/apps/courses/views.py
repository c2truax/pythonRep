from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course
import time

def index(request):
    request.session.clear()
    context = {
        "courses" : Course.objects.all()
    }
    return render(request, "courses/index.html", context)

def create(request):
    if request.method == "POST":
        errflash = Course.objects.basic_validator(request.POST)
        if len(errflash):
            for value in errflash.items():
                    messages.error(request, value)
            return redirect('/courses/')
        else:
            course = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
            course.save()
            print(course)
            return redirect('/courses/')

def confirmation(request,id):
    context = {
        "course" : Course.objects.get(id=id)
    }
    if "id" not in request.session:
        request.session['id'] = id

    return render(request, "courses/confirm.html", context)

def destroy(request):
    Course.objects.get(id=request.session['id']).delete()
    return redirect("/courses/")