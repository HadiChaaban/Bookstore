# Project Information

This project is a webapp based off of Django Python.

It is a prototype bookstore that allows for searching a catalog of books, looking at individual books, and put books into a cart.
When testing make sure Cookies ARE enabled, and you have no ad-block, so the session handling for the cart works properly.

All html files used are based off of the bootstrap framework, to allow for a better looking project while focusing more on the backend code.
The database used is SQLite3, and all handling is through Django

The project consists of 3 webapps: Core, Store, and Cart

Core is the core webapp that doesn't have any features, just stores the main configuration for URLs, HTML templates, settings, etc.

Store is the store webapp that has almost all the features from the project, excluding the cart. The store has a model named Book, containing variables for a book (title, image, etc).

Cart is the cart webapp that has its main functionality in its name. It needed to be seperate from the store webapp because it was a completely different type of application. Session handling required more views and had no models.

For testing, the project is populated with a top 300 books on Amazon csv file. To populate, the SQLite command line was used. There were other methods to do this, like migrating the data with a python function, but SQLite command line was fastest.

NO IMAGES HAVE BEEN UPLOADED TO THE PROJECT, IT IS NOT AN ERROR, THAT IS JUST A DEFAULT IMAGE. There is no reason to upload images for 300 books for testing.

# Instructions (How to run the server on your computer!)

Make sure Python 3.9.5 is installed on your computer.

WINDOWS ONLY:
Open Visual Studio Code
Go to File -> Open Folder...
Open the Bookstore-main folder
If prompted to trust authors, click trust authors
Open the terminal using Ctrl + '

'''
venv\Scripts\activate
'''
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
