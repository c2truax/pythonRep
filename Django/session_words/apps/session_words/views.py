from django.shortcuts import render, HttpResponse, redirect
import datetime
def index(request):
    
    return render(request,'session_words/index.html')

def process(request):
    if request.method == "POST":
        word = request.POST['word'] 
        radio = request.POST['radio']
        big_font = request.POST['big_font']
        date_time = str(datetime.datetime.now())
        if radio == 'red':
            radio = 'danger'
        elif radio == 'green':
            radio = 'success'
        elif radio == 'blue':
            radio = 'primary'
        if big_font == '1':
            big_font = 'bold'
        else:
            big_font = 'normal'
        if 'words' in request.session:
            words = request.session['words']
            words.append({"word": word, "color": radio, "big_font": big_font, "datetime": date_time})
            request.session['words'] = words
        else:
            words = []
            words.append({"word": word, "color": radio, "big_font": big_font, "datetime": date_time})
            request.session['words'] = words
        return redirect('/result')
    else:
        return redirect('/result')
    

def result(request):
    
    return render(request, 'session_words/index.html')

def reset(request):
    try:
        del request.session['words']
    except KeyError:
        pass
    return redirect('/')
