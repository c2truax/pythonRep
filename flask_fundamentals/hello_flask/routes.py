from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<msg>')

def say(msg):
    msg = msg.capitalize()
    if msg == 'John':
        return "Hi " + msg + "!"
    return "Hi "+ msg

@app.route('/repeat/<num>/<msg>')
def repeat(num,msg):
    num = int(num)
    return (f"<p>{msg}</p>") * num

app.run(debug = True)