from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def index(request):
    if "id" in request.session:
        return redirect('/waselApp/subjects')
    return render(request,'index.html')


def loginOrRegister(request):
    if (request.method=="POST") and (request.POST['regesterOrLogin']=="register"):
        errors = User.objects.isValid(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:

            hashedPasswd=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            
            User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],birthDate=request.POST['bday'],email=request.POST['email'],passwd=hashedPasswd)
            request.session['logedin']=True
            request.session['email'] = request.POST['email']
            thisUser=User.objects.get(email=request.POST['email'])
            request.session['id']=thisUser.id
            request.session['thisUsersName']=thisUser.fname
            return redirect('/thoughts')

    elif (request.method=="POST" and request.POST['regesterOrLogin']=="login"):
        errors = User.objects.loginValid(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            one=request.POST['email']
            two=request.POST['password']
            try:
                users = User.objects.filter(email=one)
                thisUser = users[0]
            except:
                messages.error(request, "this email doesn't exist")
                return redirect('/')
            if bcrypt.checkpw(two.encode(),thisUser.passwd.encode()):
                request.session['id']=thisUser.id
                request.session['logedin']=True
                request.session['thisUsersName']=one
                request.session['email']=one
                return redirect('/thoughts')
            else:
                messages.error(request, "I have this email but the password is NOT right")
                return redirect('/')
    return redirect('/')