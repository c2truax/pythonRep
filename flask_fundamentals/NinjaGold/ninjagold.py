from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)

app.secret_key = 'whatwhat'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activitylog'] = ''

    print(session)    
    return render_template('index.html', gold=session['gold'],activitylog = session['activitylog'])

@app.route('/process_money', methods=['POST'])
def moneybags():
    import random, datetime
    location = request.form['building']
    if location == 'farm':
        money = random.randrange(10,21)
        session['gold'] += money
    elif location == 'cave':
        money = random.randrange(5,11)
        session['gold'] += money
    elif location == 'house':
        money = random.randrange(2,6)
        session['gold'] += money
    elif location == 'casino':
        money = random.randrange(-50,51)
        session['gold'] += money
    
    if money < 0:
        money *= -1
        session['activitylog'] += (f"<p class='text-danger'>Entered a {location} and lost {money} gold...Ouch..({datetime.datetime.now()})</p>")
    else:
        session['activitylog'] += (f"<p class='text-success'>Earned {money} gold from the {location}! ({datetime.datetime.now()})</p>")
    
    if session['gold'] < 0:
        session['activitylog'] += (f"<p class='text-danger'>Watch out the Mob is coming to collect!!!!!</p>")
    
    return redirect('/')
    


if __name__==('__main__'):
    app.run(debug=True)