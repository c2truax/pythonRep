from django.shortcuts import render, HttpResponse, redirect

def index(request):
    
    return render(request,'survey/index.html')

def process(request):
    if request.method == "POST":
        if 'count' in request.session:
            request.session['count'] += 1
        else:
            request.session['count'] = 1
        request.session['name'] = request.POST['name'] 
        request.session['dojo'] = request.POST['dojo']
        request.session['favorite'] = request.POST['favorite']
        request.session['comments'] = request.POST['comments']
        return redirect('/result')
    else:
        return redirect('/result')
    

def result(request):
    print("hello")
    return render(request, 'survey/success.html')

def reset(request):
    try:
        del request.session['count']
    except KeyError:
        pass
    return redirect('/')
