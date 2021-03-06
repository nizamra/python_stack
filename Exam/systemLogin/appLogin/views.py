from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    if "logedin" in request.session:
        return redirect('/thoughts')
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
            hashedPasswd=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],birthDate=request.POST['bday'],email=request.POST['email'],passwd=hashedPasswd)
            request.session['logedin']=True
            request.session['email'] = request.POST['email']
            thisUser=User.objects.get(email=request.POST['email'])
            request.session['id']=thisUser.id
            request.session['thisUsersName']=thisUser.fname
            return redirect('/thoughts')
    elif (request.method=="POST" and request.POST['regOrLog']=="login"):
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

def welcomeThoughts(request):
    if request.session['logedin']:
        thisUsers= User.objects.get(email=request.session['email'])
        request.session['thisUsersName']=thisUsers.fname
        request.session['id']=thisUsers.id
        request.session['thisUsersLname']=thisUsers.lname
        allThoughts = Thought.objects.all()
        #allThoughts = allThoughts.order_by('likedBy').reverse()
        context={
            'Thoughts' : allThoughts,
            'hisFavs' : Thought.objects.filter(likedBy=thisUsers),
        }
        return render(request,'thoughts.html', context)

def thoughtData(request, id):
    if request.session['logedin']:
        thisUsers= User.objects.get(email=request.session['email'])
        thisThought = Thought.objects.get(id=id),
        thisThought = thisThought[0]
        q1 = User.objects.filter(likes=thisThought.id)
        notAllLikers = q1.exclude(createdThoughts=thisThought)
        context={
            'specificThought' : Thought.objects.get(id=id),
            'hisFavs' : Thought.objects.filter(likedBy=thisUsers),
            'likers' : notAllLikers
        }
        return render(request,'specificThought.html', context)

def deleteThought(request, id):
    delThought(id)
    return redirect('/')

def addThought(request):
    desc = request.POST['formDesc']
    userId = request.session['id']
    createThought(desc, userId)
    return redirect('/')

def likeThought(request, id):
    userId = request.session['id']
    likeSomeThought(id, userId)
    return redirect('/')

def unlikethisThought(request, id):
    userId = request.session['id']
    unlikeSomeThought(id, userId)
    return redirect('/')

def cleanTheSession(request):
    request.session.clear()
    return redirect('/')