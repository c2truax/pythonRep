from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)

app.secret_key = 'pssst'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    
    return render_template('index.html')

@app.route('/destroy_session')
def clearsession():
    session.clear()
    return redirect('/')

@app.route('/bytwo')
def bytwo():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('count')

    return redirect('/')



if __name__==('__main__'):
    app.run(debug=True)