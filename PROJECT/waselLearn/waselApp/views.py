from django.shortcuts import render, HttpResponse, redirect
from .models import *

def subjects(request):
    return render(request,'subjects.html')








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