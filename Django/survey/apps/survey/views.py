from django.shortcuts import render, HttpResponse, redirect

def index(request):
    
    return render(request,'survey/index.html')
