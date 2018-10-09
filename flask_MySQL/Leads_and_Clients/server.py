
from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'wazzup'
@app.route('/')
def index():
    if 'all_leads' not in session:
        mysql = connectToMySQL("lead_gen_business")
        query = "SELECT COUNT(leads.leads_id) AS 'TOTAL', CONCAT(clients.first_name, ' ', clients.last_name) AS name FROM leads JOIN sites ON leads.site_id = sites.site_id JOIN clients ON clients.client_id = sites.client_id GROUP BY CONCAT(clients.first_name, ' ', clients.last_name);"
        all_leads = mysql.query_db(query)
        print("Fetched all leads", all_leads)
        session['all_leads'] = all_leads
        session['daterange'] = 'All Dates'
    all_leads = session['all_leads']
    session.pop('all_leads')
    return render_template('index.html', all_leads = all_leads)
# 
@app.route('/date_range', methods=['POST'])
def refine():
    mysql = connectToMySQL("lead_gen_business")
    query = "SELECT COUNT(leads.leads_id) AS 'TOTAL', CONCAT(clients.first_name, ' ', clients.last_name) AS name FROM leads JOIN sites ON leads.site_id = sites.site_id JOIN clients ON clients.client_id = sites.client_id WHERE registered_datetime >= %(datestart)s AND registered_datetime <= %(dateend)s GROUP BY CONCAT(clients.first_name, ' ', clients.last_name);"
    data = { 'datestart' : request.form['datefrom'], 'dateend' : request.form['dateto']}
    all_leads = mysql.query_db(query,data)
    session['all_leads'] = all_leads
    session['daterange'] = (f"{request.form['datefrom']} - {request.form['dateto']}")  
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)