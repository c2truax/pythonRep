from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__) 
app.secret_key = "buzzjacket"
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_user():
    print("Info Submitted")
    error = ''
    for item in request.form:
        if len(request.form[item]) < 1:
            error += "<p class='text-center text-danger'>" + item + " cannot be blank!</p>"

    if not EMAIL_REGEX.match(request.form['email']):
         error += "<p class='text-center text-danger'>Email is not valid!</p>"

    mysql = connectToMySQL("mydb")
    query = "SELECT email FROM emails;"
    all_emails = mysql.query_db(query)
    print("Fetched all emails", all_emails)
    for email in all_emails:
        if request.form['email'] == email['email']:
            error += "<p class='text-center text-danger'>Email is already in the database!</p>"

    if len(error) > 0:
        flash(error)
        flash("Please correct your errors and resubmit.")
        return redirect('/')
    else:
        # flash("Thank you for registering!")
        mysql = connectToMySQL("mydb")
        query = "INSERT INTO emails(email,created_at) VALUES (%(email)s, NOW());"
        data = { 'email' : request.form['email']}
        emailid = mysql.query_db(query, data)
        if 'emailid' not in session:
            session['emailid'] = emailid
        return redirect('/success')

@app.route('/success')
def showemails():
    emailid = int(session['emailid'])
    print("\n\n", emailid,  "\n\n")
    
    mysql = connectToMySQL("mydb")
    query = "SELECT email FROM emails WHERE id = %(eid)s;"
    data = { 'eid' : session['emailid']}
    new_email = mysql.query_db(query,data)
    print(new_email)
    session.pop('emailid')

    mysql = connectToMySQL("mydb")
    query = "SELECT email, created_at FROM emails;"
    all_emails = mysql.query_db(query)
    return render_template("success.html", new_email = new_email, all_emails = all_emails)

# @app.route('/delete')
# def deleteRecord():
#     mysql = connectToMySQL("mydb")
#     query = "DELETE FROM emails WHERE ;"
#     mysql.query_db(query)


if __name__=='__main__':
    app.run(debug=True)