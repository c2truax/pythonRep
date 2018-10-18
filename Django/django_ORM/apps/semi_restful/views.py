from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
def index(request):
    request.session.clear()
    context = {}
    context['users'] = User.objects.all()
    return render(request, 'semi_restful/index.html', context=context)

def new(request):
    return render(request, 'semi_restful/add_user.html')

def edit(request,id):
    if "id" not in request.session:
        request.session["id"] = id
    return render(request, 'semi_restful/edit_user.html')

def show(request,id):
    context = {
        "user" : User.objects.get(id=id)
    }
    return render(request, 'semi_restful/show_user.html', context=context)


def update(request):
    if request.method == 'POST':
        user = User.objects.get(id=int(request.session["id"]))
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        id = str(user.id)
        return redirect('/semi_restful/users/'+id)

def create(request):
    if request.method == 'POST':
        user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'])
        user.save()
        id = str(user.id)
    return redirect("../"+ id + "/")

def destroy(request,id):
    User.objects.get(id=id).delete()
    return redirect('../../')