from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re, datetime
from datetime import *
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'huh'
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    mysql = connectToMySQL("walldb")
    query = 'SELECT * FROM user;'
    users = mysql.query_db(query)
    return render_template('index.html')

@app.route('/createUser', methods=['Post'])
def process():

    if len(request.form['first_name']) < 2:
        flash('First Name Required', 'first_name')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash('First Name cannot contain numbers or symbols', 'first_name')

    if len(request.form['last_name']) < 2:
        flash('Last Name Required', 'last_name')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash('Last Name cannot contain numbers', 'last_name')

    if len(request.form['email']) <1:
        flash('Email cannot be blank!', 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!', 'email')
    mysql = connectToMySQL("walldb")
    query = "SELECT email FROM user WHERE email = %(email)s;"
    data = {'email': request.form['email']}
    login_email = mysql.query_db(query, data)    
    if len(login_email) > 0:
            flash('Email already in database', 'email')

    if len(request.form['password']) < 8:
        flash('Password must be at least 8 characters', 'password')
    if re.search('[A-Z]', request.form['password']) is None:
        flash('Password must contain at least one capital letter', 'password')
    if re.search('[0-9]', request.form['password']) is None:
        flash('Password must contain at least one number', 'password')
    elif request.form['password'] != request.form['passconfirm']:
        flash('Passwords do not match', 'password')
    
    if '_flashes' in session.keys():
        return redirect('/')
    else:

        pwd = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL('walldb')
        query = 'INSERT INTO user(first_name, last_name, email, password, created_at, updated_at, user_level) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW(), 1);'
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pwd
        }
        newuser = mysql.query_db(query, data)
        flash('You have been successfully registered', 'success')
        if 'userid' not in session:
            session['userid'] = newuser
            session['name'] = request.form['first_name']
        return redirect('/success')

@app.route('/success')
def success():
    if 'userid' not in session:
        return redirect('/')
    mysql = connectToMySQL('walldb')
    query = 'SELECT user.first_name AS name, message.message AS message, message.created_at AS created_at, message.id AS mid FROM message JOIN user ON user.id = message.user_id WHERE message.recipient_id = %(id)s ORDER BY message.created_at DESC;'
    data = {
            'id': session['userid']
        }
    sents = mysql.query_db(query, data)

    for i in range(len(sents)):
        sents[i]['sent_at'] = datetime.now() - sents[i]['created_at']
        sents[i]['sent_at'] = sents[i]['sent_at'].seconds
        if int(sents[i]['sent_at']/60/60) < 24:
            sents[i]['sent_at'] = str(int(sents[i]['sent_at']/60/60)) + ' hours ago'
        elif int(sents[i]['sent_at']/60/60/24) < 30:
            sents[i]['sent_at'] = str(int(sents[i]['sent_at']/60/60/24)) + ' days ago' 
        elif int(sents[i]['sent_at']/60/60/24/30) < 12:
            sents[i]['sent_at'] = str(int(sents[i]['sent_at']/60/60/24/30)) + ' months ago'
        else:
            sents[i]['sent_at'] = sents[i]['created_at']

    if 'sents' not in session:
        session['sents'] = sents
    receivecount = 0
    if 'receivecount' not in session:
        for sent in sents:
            receivecount += 1
    
        session['receivecount'] = receivecount

    mysql = connectToMySQL('walldb')
    query = 'SELECT * FROM user WHERE id != %(id)s AND id != 1 ORDER BY id DESC;'
    data = {
            'id': session['userid']
        }
    recipients = mysql.query_db(query, data)
    if 'recipients' not in session:
        session['recipients'] = recipients
    
    mysql = connectToMySQL('walldb')
    query = "SELECT COUNT('message') AS count FROM message WHERE user_id = %(id)s;"
    data = {
            'id': session['userid']
        }
    messages = mysql.query_db(query, data)
    print("Printing the count SQL", messages)
    sendcount = messages[0]['count']
    if 'sendcount' not in session:
        session['sendcount'] = sendcount
    
    return render_template('success.html')



@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL('walldb')
    query = 'SELECT * FROM user WHERE email = %(email)s;'
    data = {
            'email': request.form['username']
        }
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['pw']):
            session['userid'] = result[0]['id']
            session['name'] = result[0]['first_name']
            session['user_level'] = result[0]['user_level']
            if result[0]['user_level'] == 1:
                return redirect ('/success')
            elif result[0]['user_level'] == 9:
                return redirect ('/admin')
    flash('You could not be logged in', 'login')
    return redirect('/')

@app.route('/admin')
def admin():
    if 'userid' not in session:
        return redirect('/')
    mysql = connectToMySQL('walldb')
    query = 'SELECT user_level FROM user WHERE id = %(userid)s'
    data = { 'userid' : session['userid']}
    validate = mysql.query_db(query, data)
    if validate[0]['user_level'] != session['user_level']:
        return redirect('/danger')
    else:
        mysql = connectToMySQL('walldb')
        query = 'SELECT * FROM user;'
        adminpage = mysql.query_db(query)
        session['adminpage'] = adminpage
        return render_template('admin.html')

@app.route('/sendmessage', methods=['POST'])
def message():
    
    mysql = connectToMySQL('walldb')
    query = 'INSERT INTO message(message, user_id, recipient_id, created_at, update_at) VALUES (%(message)s, %(user_id)s, %(recipient_id)s, NOW(), NOW());'
    data = {
        'message': request.form['message'],
        'user_id': session['userid'],
        'recipient_id' : request.form['recipientid']
    }
    newmessageid = mysql.query_db(query, data)
    session.pop('recipients')
    session.pop('sendcount')
    flash('Message Sent!', 'success')
    return redirect('/success')

@app.route('/sent')
def sent():
    return render_template('success.html')

@app.route('/delete', methods=['POST'])
def deleteMessage():
    mysql = connectToMySQL('walldb')
    query = 'SELECT recipient_id FROM message WHERE id = %(mid)s;'
    data = { 'mid' : request.form['deleteid'] }
    idmatch = mysql.query_db(query, data)
    if session['userid'] != idmatch[0]['recipient_id']:
        if 'warn' not in session:
            session['warn'] = True 
            session['messid'] = request.form['deleteid']      
            return redirect('/danger')
        else:
            return redirect('/logout')

    mysql = connectToMySQL('walldb')
    query = 'UPDATE message SET recipient_id = 1 WHERE id = %(mid)s;'
    data = { 'mid' : request.form['deleteid'] }
    mysql.query_db(query, data)
    session.pop('sents')
    session.pop('receivecount')
    return redirect('/success')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/danger')
def danger():
    ipaddress = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return render_template('danger.html', ipaddress=ipaddress)
    
    
if __name__=="__main__":
    app.run(debug=True)