# friends_flask_mysql

Create an application that will perform all the CRUD operations on the friends resource:

In Index.html, each friend should have an "edit" button that will take the user to the '/friends/<id>/edit' URL which should display the edit page for that particular user

The edit page form should send a POST request to '/friends/<id>' which will actually update the user in the database with the new inputs

In Index.html, each friend should have a "delete" button (part of a form) that should POST to '/friends/<id>/delete'
This route should delete the user from the database

At this point, you should have 2 pages and 5 routes which should be handled by the routes and methods below

Method	  URL	                    Route Handler Function	  Purpose
GET	      '/'	                      index()	                  Display all of the friends on the index.html page
POST    	'/friends'	              create()	                Handle the add friend form submit and create the friend in the DB
GET	      '/friends/<id>/edit'	    edit(id)	                Display the edit friend page for the particular friend
POST      '/friends/<id>'	          update(id)	              Handle the edit friend form submit and update the friend in the DB
POST	    '/friends/<id>/delete'	  destroy(id)	              Delete the friend from the DB

Make sure that your application uses the structure above.
