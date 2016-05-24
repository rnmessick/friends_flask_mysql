from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    query = "SELECT id, concat(first_name, ' ', last_name) as name FROM friends" # define your query
    friends = mysql.query_db(query) # run the query with the query_db method
    return render_template('index.html', all_friends=friends) # pass the data to our template

@app.route('/friends', methods=['POST'])
def create():
    # write our query as a string, notice how we have multiple values we want to
    # insert into our query
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    # we'll then create a dictionary of data from the POST data received
    data = {
           'first_name': request.form['first_name'],
           'last_name':  request.form['last_name'],
           'occupation': request.form['occupation']
           }
    # run the query with the dictionary values injected into the query
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>', methods=['POST', 'GET'])
def update(id):
    # Figure out the HTTP verb. If it's a GET, we want to render a page that shows user information.
    if request.method == "GET":
        # Get friend from database
        query = "SELECT id, concat(first_name, ' ', last_name) as name, occupation FROM friends WHERE id = :id"
        data = { 'id' : id }
        friend = mysql.query_db(query, data)[0]
        return render_template('show.html', friend=friend)
    # If we're here, it's a POST
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
           'first_name': request.form['first_name'],
           'last_name':  request.form['last_name'],
           'occupation': request.form['occupation'],
           'id': id
           }
    mysql.query_db(query, data)
    return redirect('/friends/'+id)

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect("/")
app.run(debug=True)
