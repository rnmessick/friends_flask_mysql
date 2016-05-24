from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends" # define your query
    friends = mysql.query_db(query) # run the query with the query_db method
    return render_template('index.html', all_friends=friends) # pass the data to our template

@app.route('/friends', methods=['POST'])
def create():
    print request.form
    # write our query as a string, notice how we have multiple values we want to
    # insert into our query
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"

    print query
    # we'll then create a dictionary of data from the POST data received
    data = {
           'first_name': request.form['first_name'],
           'last_name':  request.form['last_name'],
           'occupation': request.form['occupation']
           }
    print "DATA", data
    # run the query with the dictionary values injected into the query
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
           'first_name': request.form['first_name'],
           'last_name':  request.form['last_name'],
           'occupation': request.form['occupation'],
           'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect("/")
app.run(debug=True)
