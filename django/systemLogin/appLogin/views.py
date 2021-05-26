from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    if "logedin" in request.session:
        return HttpResponse(f"You are logged in as {request.session['thisUsersName']}")
    context={
        'allUsers' : User.objects.all()
    }
    return render(request,'index.html', context)

def loginOrRegister(request):
    if (request.method=="POST") and (request.POST['regOrLog']=="register"):
        errors = User.objects.isValid(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],birthDate=request.POST['bday'],email=request.POST['email'],passwd=request.POST['password'])
            request.session['logedin']=True
            request.session['email'] = request.POST['email']
            x=User.objects.get(email=request.POST['email'])
            num=x.id
            return redirect('/success/'+str(num))
    elif (request.method=="POST" and request.POST['regOrLog']=="login"):
        one=request.POST['email']
        two=request.POST['password']
        try:
            thisUser = User.objects.get(email=one)
        except:
            return HttpResponse("You are DOOMED HAHAHAHAHAHA... this email doesn't exist")
        if thisUser.passwd==two:
            request.session['logedin']=True
            request.session['thisUsersName']=one
            request.session['email']=one
            return HttpResponse(f"I have this email and its a correct password belonging to Mr {thisUser.fname} {thisUser.lname}")
        else:
            return HttpResponse("I have this email but the password is NOT right")
    return redirect('/')

def successPage(request):
    if request.session['logedin']:
        thisUsers= User.objects.get(email=request.session['email'])
        request.session['thisUsersName']=thisUsers.fname
        request.session['thisUsersLname']=thisUsers.lname
        return render(request,'success.html')

def cleanTheSession(request):
    request.session.clear()
    return redirect('/')