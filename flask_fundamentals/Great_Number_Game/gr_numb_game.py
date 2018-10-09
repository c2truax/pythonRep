from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)

app.secret_key = 'pssst'

@app.route('/')
def index():
    import random
    if 'random' in session:
        pass
    else:
        random = random.randrange(1, 101)
        print(random)
        session['random']= random

    return render_template('index.html', hidden ='d-none', success = 'd-none', hideform = '')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guessbox'])
    print(request.form)
    if guess == int(session['random']):
        print('correct')
        random = session['random']
        session.pop('random')
        return render_template('index.html', success = 'd-block', random = random, hidden = 'd-none', hideform = 'd-none')
    elif guess < int(session['random']):
        print('too low')
        return render_template('index.html', hidden='', wrong='Low', success = 'd-none', hideform = '')
    elif guess > int(session['random']):
        print('too high')
        return render_template('index.html', hidden='', wrong='High', success = 'd-none', hideform = '')
    
    return redirect('/')





if __name__==('__main__'):
    app.run(debug=True)