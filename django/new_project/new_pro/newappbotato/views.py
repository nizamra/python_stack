from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
def form(request):
    return render(request,'form.html')
def root(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def name(request,name):
    return HttpResponse(f"Hello dear {name} hope you're having fun")
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
        "time": strftime("%a, %Y-%m-%d %H:%M %p", localtime())
    }
    return render(request,"time.html", context)
def result(request):
    nome=request.POST["nome"]
    locale=request.POST["locale"]
    longage=request.POST["longage"]
    cremlent=request.POST["cremlent"]
    context ={
        "nome":nome,
        "locale":locale,
        "longage":longage,
        "cremlent":cremlent
    }
    if request.method == "GET":
    	print("a GET request is being made to this route")
    	return HttpResponse("sorry we don't deal with GET req")
    if request.method == "POST":
        print("a POST request is being made to this route")
        return render(request,"result.html", context)
        
def secondform(request):
    request.session['neam'] = request.POST['neam']
    request.session['email'] = request.POST['email']
    request.session['pswd'] = request.POST['pswd']
    request.session['cmnt'] = request.POST['cmnt']
    return redirect("/showdata")
def showdata(request):
    return render(request,"datatwo.html")

def countthem(request):
    request.session['visitingNumber'] = int(request.session.get('visitingNumber',0)) +1
    return render(request, "cnt.html")
def destroy(request):
    request.session.clear()
    return redirect("/counter")

    
