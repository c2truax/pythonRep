from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__) 
app.secret_key = "fuzzywuzzy"
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_user():
    print("Info Submitted")
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!")
    elif len(request.form['comments']) < 1:
        flash("Comments cannot be blank!")
    elif len(request.form['comments']) > 121:
        flash("Comments must be 120 characters or less!")
    else:
        session.clear()
        return render_template('success.html')

    return redirect('/')
@app.route('/danger')
def danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)