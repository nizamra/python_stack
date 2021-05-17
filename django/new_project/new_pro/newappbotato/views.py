from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
def root(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request,number):
    return HttpResponse(f"placeholder to display blog number{number} ")
def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")
def destroy(request,number):
    return redirect("/blogs")
def time(request):
    context  = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,"time.html", context)


    
