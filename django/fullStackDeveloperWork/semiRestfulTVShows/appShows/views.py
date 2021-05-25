from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    if "logedin" in request.session:
        return HttpResponse(f"You are logged in as {request.session['name']}")
    context={
        'allShows' : Show.objects.all()
    }
    return render(request,'shows.html', context)

def showsNewPage(request):
    return render(request, 'showsNew.html')

def recordShow(request):
    if request.method=="POST":
        Show.objects.create(title=request.POST['titleField'],network=request.POST['networkField'] ,releaseDate=request.POST['releaseDateField'] ,description=request.POST['descriptionField'])
        x=Show.objects.get(title=request.POST['titleField'])
        num=x.id
        return redirect('/shows/'+str(num))
def updateShow(request,showId):
    if request.method=="POST":
        thisShow=Show.objects.get(id=showId)
        thisShow.title=request.POST['titleField']
        thisShow.network=request.POST['networkField']
        thisShow.releaseDate=request.POST['releaseDateField']
        thisShow.description=request.POST['descriptionField']
        thisShow.save()

        num=thisShow.id
        return redirect('/shows/'+str(num))

def displayShow(request,showId):
    context={
        'thisShow' : Show.objects.get(id=showId)
    }
    return render(request,'showsSpecific.html', context)

def editShow(request,showId):
    context={
        'thisShow' : Show.objects.get(id=showId)
    }
    return render(request,'showsEdit.html', context)
def deleteShow(request,showId):
    thisShow= Show.objects.get(id=showId)
    thisShow.delete()
    return redirect('/')


def cleanAllData(request):
    x=Show.objects.all()
    x.delete()
    request.session.clear()
    return redirect('/')