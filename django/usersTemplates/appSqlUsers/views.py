from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        "people": User.objects.all()
    }
    return render(request, "index.html", context)

def indixingTheSql(request):
    User.objects.create(fname =request.POST["userName"],lname =request.POST["userLastName"],email =request.POST["mail"],age =request.POST["age"])
    return redirect("/")