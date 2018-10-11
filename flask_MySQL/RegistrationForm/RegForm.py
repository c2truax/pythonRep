from flask import Flask, render_template, redirect, request, session, flash
import re, datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__) 
app.secret_key = "fuzzwashere"
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_user():
    print("Info Submitted")
    error = ''
    for item in request.form:
        print(item)
        print(len(request.form[item]))
        if len(request.form[item]) < 1:
            error += "<p class='text-center text-danger'>" + item + " cannot be blank!</p>"
    if len(error) > 0:
        flash(error)
        flash("Please correct your errors and resubmit.")
        return redirect('/')    

    if not EMAIL_REGEX.match(request.form['email']):
         error += "<p class='text-center text-danger'>Email is not valid!</p>"

    if request.form['first_name'].isalpha() == False:
        error += "<p class='text-center text-danger'>First Name should only be alphabetic characters!</p>"
 
    if request.form['last_name'].isalpha() == False:
        error += "<p class='text-center text-danger'>Last Name should only be alphabetic characters!</p>"
 
    if len(request.form['password']) < 9:
        error += "<p class='text-center text-danger'>Password should be more than 8 characters!</p>"
    elif request.form['password'] != request.form['pw_confirm']:
        error += "<p class='text-center text-danger'>Password does not match PW Confirm!</p>"
    #Ninja Validation
    elif request.form['password'].isdigit():
        error += "<p class='text-center text-danger'>Password needs at least one upper case alpha character!</p>"
    elif request.form['password'].islower():
        error += "<p class='text-center text-danger'>Password needs at least one upper case character!</p>"
    elif request.form['password'].isalpha():
        error += "<p class='text-center text-danger'>Password needs at least one numeric character!</p>"
    #Hacker Validation
    currentDT = datetime.datetime.now()
    birthdate = request.form['birth_date']
    print(birthdate)
    yyyy,mm,dd = birthdate.split('-')
    dd=int(dd)
    mm=int(mm)
    yyyy=int(yyyy)
    currentday = int(currentDT.strftime("%d"))
    currentmonth = int(currentDT.strftime("%m"))
    currentyear = int(currentDT.strftime("%Y"))
    
    if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
        max1=31
    elif(mm==4 or mm==6 or mm==9 or mm==11):
        max1=30
    elif(yyyy%4==0 and yyyy%100!=0 or yyyy%400==0):
        max1=29
    else:
        max1=28
    
    if(mm<1 or mm>12):
        error += "<p class='text-center text-danger'>The month in your input birth date is not valid!</p>"
    elif(dd<1 or dd>max1):
        error += "<p class='text-center text-danger'>The day in your input birth date is not valid!</p>"
    
    if yyyy == currentyear - 18:
        if mm >= currentmonth:
            if dd > currentday:
                error += "<p class='text-center text-danger'>The input birth date is not valid, you must be at least 18 years old!</p>"
    elif yyyy > currentyear - 18:
        error += "<p class='text-center text-danger'>The input birth date is not valid, you must be at least 18 years old!</p>"
    
    if len(error) > 0:
        flash(error)
        flash("Please correct your errors and resubmit.")
    else:
        flash("Thank you for registering!")

    return redirect('/')
@app.route('/danger')
def danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)