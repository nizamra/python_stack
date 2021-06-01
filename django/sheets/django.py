..\..\..\my-environments\djangoEnv\Scripts\activate

Django
#1. create virtual environment, activate it, then install Django inside it
python -m venv djangoPy3Env
call djangoPy3Env\Scripts\activate 
pip install Django

#2. Create your project in some directories, then go to the project folder, as follows:
django-admin startproject your_project_name_here
cd your_project directory

# 4. For every app we want to add to our project, we'll do the following:
python manage.py startapp your_app_name_here
md appWall\templates appWall\static
touch appWall\templates\index.html appWall\static\style.css
code .

# 5. for file settings.py, add the App to the  INSTALLED_APPS dictionary as follows:
INSTALLED_APPS = [
    'YOUR_APP_NAME_HERE',

# 6. in the project  urls.py, add URL of your app
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('YOUR_APP_NAME_HERE.urls')),
]

# 7. in the App, create file called urls.py, add the URL
from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    # path('logreg', views.loginOrRegister),
    # path('books/<str:bookNumber>', views.showBookData),
    # path('authors/<int:authId>', views.showauthorData),
    

    # path('cleanData', views.cleanAllData),
    # path('cleanSql', views.cleanAllSql),
    path('cleanSession', views.cleanTheSession),
]


# then in our app's views.py file, put a function called index 
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def index2(request):
    if "logedin" in request.session:
        return HttpResponse(f"You are logged in as {request.session['name']}")
    context={
        'allBooks' : Book.objects.all()
    }
    return render(request,'index.html', context)

def loginOrRegister(request):
    if (request.method=="POST") and (request.POST['regOrLog']=="register"):
        one=request.POST['fname']
        two=request.POST['lname']
        three=request.POST['email']
        four=request.POST['password']
        five=request.POST['repassword']
        if four!=five:
            return HttpResponse("You IDIOT PICE OF SHIT Didn't Provide the same PASSWORD in the second field")
        else:
            
            User.objects.create(fname=one,lname=two,email=three,passwd=four)
            request.session['logedin']=True
            request.session['name']=one
            return HttpResponse(f"You have done a good job adding new regester for {request.session['name']}")
    elif (request.method=="POST" and request.POST['regOrLog']=="login"):
        one=request.POST['email']
        two=request.POST['password']
        try:
            thisUser = User.objects.get(email=one)
        except:
            return HttpResponse("You are DOOMED HAHAHAHAHAHA... this email doesn't exist")
        if thisUser.passwd==two:
            request.session['logedin']=True
            request.session['name']=one
            return HttpResponse(f"I have this email and its a correct password belonging to Mr {thisUser.fname} {thisUser.lname}")
        else:
            return HttpResponse("I have this email but the password is NOT right")
    return redirect('/')

def addingsomeBook(request):
    if request.method=="POST":
        one=request.POST['bookName']
        two=request.POST['description']
        Book.objects.create(title=one,description=two)
    return redirect('/')
def showauthorData(request,authId):
    context={
        'myauthor' : Author.objects.get(id=authId)
    }
    return render(request,'authorData.html', context)


def cleanAllData(request):
    x=User.objects.all()
    x.delete()
    x=Book.objects.all()
    x.delete()
    x=Author.objects.all()
    x.delete()
    request.session.clear()
    return redirect('/')
def cleanAllSql(request):
    x=User.objects.all()
    x.delete()
    x=Book.objects.all()
    x.delete()
    x=Author.objects.all()
    x.delete()
    return redirect('/')
def cleanTheSession(request):
    request.session.clear()
    return redirect('/')


# 8. inside the appfile create templates\index.html
	<meta name="keywords" content="HTML, CSS, JavaScript">
	<meta name="description" content="Basic html code">
	<meta name="author" content="Nizam Aljawabreh">
	<!-- <meta http-equiv="refresh" content="30">-->

	# 1. inside the appfile create static\css\style.css
	{% load static %}
	<link rel="stylesheet" href="{% static 'css/style.css' %}">    
	<script src="{% static 'js/script.js' %}"></script>

<div style="overflow:scroll;color:blue; background-color:gray; height:150px; max-width:450px">
<table style="width:70%">
    <caption>Firstname Lastname age</caption>
    <tr>
      <th colspan="2">Firstname Lastname</th>
      <th>Age</th>
    </tr>
	{% for user in allUsers %}
		<tr>
			<td>{{ user.id }}</td>
			<td>{{ user.email }}</td>
			<td>{{ user.passwd }}</td>
			<td><a href="books/{{ elmnt.id }}">view</a></td>
		</tr>
	{% endfor %}
</table>
</div>

<button onclick="document.location='https://www.google.com'">reach google</button>
<button onclick="alert('Hello You')">alert</button>
<a href="/cleanData">Clear All SQL Database to start over</a>
<form action="/actionPage" method="POST" id="myFirstForm">
	{% csrf_token %}
	<fieldset>
		<legend>Personalia:</legend>
		<input type="hidden" name="whichForm" value="register" >

		<label for="thisID">First name:</label><br>
		<input type="text" id="thisID" name="fname" title="Your first name please Sir" autofocus required><br>
		
		<label for="passID">password Here Please:</label><br>
		<input type="password" id="passID" name="password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[-!@#$%^&*()+]).{8,12}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 characters max 12" required><br>

		<input type="number" id="ageInNumbers" name="age" placeholder="23" maxlength="4" size="4">
		<label for="thisEmail">Enter your email:</label>
		<input type="email" id="thisEmail" name="email"><br>
		<label for="someBirthday">Birthday:</label>
		<input type="date" id="someBirthday" name="birthday"><br>

		<textarea name="message" rows="10" cols="30">
			The cat was playing in the garden.
		</textarea>

		<input type="checkbox" id="vehicleOpel" name="vehicle1" value="opel">
    	<label for="vehicleOpel"> I have an Opel car</label><br>
		<input type="checkbox" id="vehicleBMWX" name="vehicle2" value="BMW">
    	<label for="vehicleBMWX"> I have a BMW car</label><br>

		<input type="radio" id="maleButton" name="gender" value="male">
    	<label for="maleButton">Male</label><br>

		<select id="cars" name="cars">
			<option value="volvo">Volvo</option>
			<option value="saab">Saab</option>
			<option value="fiat">Fiat</option>
			<option value="audi" selected>Audi</option>
			<option value="saab">meredes</option>
			<option value="fiat">mazda</option>
		</select>

		# this field still needs some revision
			# <input list="browsers">
			# <datalist id="browsers">
			# 	<option value="Internet Explorer">
			# 	<option value="Firefox">
			# 	<option value="Chrome">
			# </datalist>

		<input type="submit" value="Submit">
		<input type="reset" value="Empty to Fill Again">
	</fieldset>
</form>

# On MANYTOMANY relatins inside the HTML
Title:{{ thisBook.title }} <br>
Id: {{ thisBook.id }} <br>
description:{{ thisBook.description }} <br>
authors: <br>
{% for oneAuthor in thisBook.authors.all %}
	<p>{{ oneAuthor.fname }}</p>
{% endfor %}


# 9. creating Models CAPITALIZED
from django.db import models
import os
import re

class userManager(models.Manager):
    def isValid(self, formPOST):
        errors={}
        nameRegex = re.compile(r'([a-zA-Z]).{2,22}')
        if not nameRegex.match(formPOST["fname"]):
            errors["name"] = "name should be at least 2 characters"
        if not nameRegex.match(formPOST["lname"]):
            errors["lastName"] = "name should be at least 2 characters"
        if len(formPOST['bday']) < 2:
            errors["bday"] = "birth day should be at least 2 characters"
        
        emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailRegex.match(formPOST['email']):
            errors['email'] = "Invalid email address!!"

        try:
            thisShow=User.objects.get(email=formPOST['email'])
            errors["retitle"] = "this email is already registered"
        except:
            pass

        passwdRegex = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[-!@#$%^&*()+]).{8,12}')
        if not passwdRegex.match(formPOST["password"]):
            errors['pass'] = "Password Must contain at least one number, one uppercase, lowercase letter, and at least 8 characters max 12"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    #one to many relashion
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)

class Author(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    birthDate = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(book, related_name="authors")
    
class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = userManager()

my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))
Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello')
lil_books = Book.objects.filter(title__startswith="Little")

books = Book.objects.filter(author__name="Louise May Alcott")
books = Book.objects.filter(author__name__contains="Al")

books = Book.objects.filter(author=Author.objects.get(id=2))

age = models.IntegerField(default=200)	# if no age is entered for a new/existing, age will be set to 200
age = models.IntegerField(null=True)	# if no age is provided, the field will remain empty



this_book = Book.objects.get(id=4)	# retrieve an instance of a book
this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher

this_publisher.books.add(this_book)		# add the book to this publisher's list of books
this_book.publishers.add(this_publisher)	# add the publisher to this book's list of publishers

this_publisher.books.remove(this_book)		# remove the book from this publisher's list of books
this_book.publishers.remove(this_publisher)	# remove the publisher from this book's list of publishers

this_publisher.books.all()	# get all the books this publisher is publishing
this_book.publishers.all()	# get all the publishers for this book

-------------------------------------------------
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
-------------------------------------------------


request.session['key']
#This will retrieve (get) the value associated with 'key'
request.session['key'] = 'value'
#Set the value that will be stored by 'key' to 'value'
'key' in request.session
#Returns a boolean of whether a key is in session or not
{{ request.session.name }}
#Use dot notation (.) to access request.session keys from templates since square brackets ([]) aren’t allowed there
del request.session['key']
#Deletes a session key if it exists, throws a KeyError if it doesn’t. Use along with try and except since it's better to ask for #forgiveness than permission
#Note: If you are storing a list in session that is being modified (such as an append), you will need to save the session after #the append, like so:
request.session['my_list'] = []
request.session['my_list'].append("new item")
request.session.save()

# On CLASS to add a relation
bookNum2=book.objects.get(id=2)
authorNum3=author.object.get(id=3)
authorNum3.authors.add(bookNum2)


“Don’t delete. Just don’t.”
use a field containing the status of the related data: active, discontinued, cancelled, deprecated
 #search for this one and more options for all
        #status = models.TextChoices()
		#status = models.TextChoices(default=active, discontinued, cancelled, deprecated)
		

<script>
	function checkValidation() {
		var val = $('#username').val()
		if(val == "") {
			$('#username-error').css('display', 'block')
		}
		else {
			$('#login-form').submit()
		}
	}
</script>





python -m ensurepip
(djangoEnv) D:\codingdojo\python_stack\django\fullStackDeveloperWork\theWall>python -m ensurepip
Looking in links: c:\Users\NIZAM\AppData\Local\Temp\tmpoyijun1q
Requirement already satisfied: setuptools in d:\codingdojo\python_stack\my-environments\djangoenv\lib\site-packages (49.2.1)
Processing c:\users\nizam\appdata\local\temp\tmpoyijun1q\pip-20.2.3-py2.py3-none-any.whl
Installing collected packages: pip
Successfully installed pip-20.2.3

pip list
Package    Version
---------- -------
-ip        20.2.3
asgiref    3.3.4
bcrypt     3.2.0
cffi       1.14.5
Django     3.2.3
pip        20.2.3
pycparser  2.20
pytz       2021.1
setuptools 49.2.1
six        1.16.0
sqlparse   0.4.1