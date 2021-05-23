from django.shortcuts import render,redirect
from .models import Dojo,Ninja

# Create your views here.
def index(request):
    context={
        'data' : Dojo.objects.all()
    }
    return render(request, 'index.html', context)
def inputsql(request):
    if request.POST['whatForm']=="dojo":
        one=request.POST['dojoname']
        cit=request.POST['city']
        sta=request.POST['state']
        des=request.POST['desc']
        Dojo.objects.create(name=one,city=cit,state=sta, desc=des)
    elif request.POST['whatForm']=="ninja":
        somename=request.POST['ninjaFname']
        somefamily=request.POST['lname']
        whatDojo=request.POST['dojoId']
        Ninja.objects.create(fname=somename,lname=somefamily,dojoId=Dojo.objects.get(name=whatDojo))
        
    return redirect('/')

def clear(request):
    x=Dojo.objects.all()
    x.delete()
    x=Ninja.objects.all()
    x.delete()
    return redirect('/')