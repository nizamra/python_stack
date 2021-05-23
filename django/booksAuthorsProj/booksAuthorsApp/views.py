from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):
    context={
        'allBooks' : book.objects.all()
    }
    return render(request,'index.html', context)
def authorsPage(request):
    context={
        'allauthors' : author.objects.all()
    }
    return render(request,'authors.html', context)


def addingsomeBook(request):
    if request.method=="POST":
        one=request.POST['bookName']
        two=request.POST['description']
        book.objects.create(title=one,description=two)
    return redirect('/')
def addingNewAuthor(request):
    if request.method=="POST":
        one=request.POST['authorName']
        two=request.POST['lname']
        author.objects.create(fname=one,lname=two)
    return redirect('/authors')


def showBookData(request,bookNumber):
    context={
        'myBook' : book.objects.get(id=bookNumber)
    }
    return render(request,'BookData.html', context)
def showauthorData(request,authId):
    context={
        'myauthor' : author.objects.get(id=authId)
    }
    return render(request,'authorData.html', context)

def cleanAll(request):
    x=book.objects.all()
    x.delete()
    x=author.objects.all()
    x.delete()
    return redirect('/')