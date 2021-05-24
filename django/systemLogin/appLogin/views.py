from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):
    if "logedin" in request.session:
        return HttpResponse(f"You are logged in as {request.session['name']}")
    context={
        'allUsers' : user.objects.all()
    }
    return render(request,'index.html', context)
# def authorsPage(request):
#     context={
#         'allauthors' : author.objects.all()
#     }
#     return render(request,'authors.html', context)


def loginOrRegister(request):
    if (request.method=="POST") and (request.POST['regOrLog']=="register"):
        one=request.POST['fname']
        two=request.POST['lname']
        three=request.POST['email']
        four=request.POST['password']
        five=request.POST['repassword']
        if four!=five:
            return HttpResponse("You IDIOT PICE OF SHIT Didn't Provide the same PASSWORD in the second field")
        else:
            
            user.objects.create(fname=one,lname=two,email=three,passwd=four)
            request.session['logedin']=True
            request.session['name']=one
            return HttpResponse(f"You have done a good job adding new regester for {request.session['name']}")
    # elif (request.method=="POST" and request.POST['regOrLog']=="login"):
    #     one=request.POST['email']
    #     two=request.POST['password']
    #     users = user.objects.all()
    #     for someuser in users:
    #         if one in someuser.email:
    #             if someuser.passwd==two:
    #                 request.session['logedin']=True
    #                 request.session['name']=one
    #                 return HttpResponse(f"I have this email and its a correct password belonging to Mr {someuser.fname} {someuser.lname}")
    #             else:
    #                 return HttpResponse("I have this email but the password is NOT right")
    #         else:
    #             return HttpResponse("I do NOT have this email")
    elif (request.method=="POST" and request.POST['regOrLog']=="login"):
        one=request.POST['email']
        two=request.POST['password']
        try:
            thisUser = user.objects.get(email=one)
        except:
            return HttpResponse("You are DOOMED HAHAHAHAHAHA... this email doesn't exist")
        if thisUser.passwd==two:
            request.session['logedin']=True
            request.session['name']=one
            return HttpResponse(f"I have this email and its a correct password belonging to Mr {thisUser.fname} {thisUser.lname}")
        else:
            return HttpResponse("I have this email but the password is NOT right")

        

    return redirect('/')

# def showBookData(request,bookNumber):
#     context={
#         'myBook' : book.objects.get(id=bookNumber)
#     }
#     return render(request,'BookData.html', context)
# def showauthorData(request,authId):
#     context={
#         'myauthor' : author.objects.get(id=authId)
#     }
#     return render(request,'authorData.html', context)

def cleanAllData(request):
    x=user.objects.all()
    x.delete()
    request.session.clear()
    return redirect('/')
def cleanAllSql(request):
    x=user.objects.all()
    x.delete()
    return redirect('/')
def cleanTheSession(request):
    request.session.clear()
    return redirect('/')