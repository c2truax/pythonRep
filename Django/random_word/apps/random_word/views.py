from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
        "word": get_random_string(length=14)
    }
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 0
    

    return render(request,'random_word/index.html', context)

def reset(request):
    request.session['count'] = -1
    return redirect('/')