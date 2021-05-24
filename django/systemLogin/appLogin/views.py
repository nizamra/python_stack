from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):
    return render(request,'index.html')
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
    elif (request.method=="POST" and request.POST['regOrLog']=="login"):
        one=request.POST['email']
        two=request.POST['password']
        users = user.objects.all()
        for someuser in users:
            if one in someuser.email:
                if someuser.passwd==two:
                    return HttpResponse(f"I have this email and its a correct password belonging to Mr {someuser.fname} {someuser.lname}")
                else:
                    return HttpResponse("I have this email but the password is NOT right")
            else:
                return HttpResponse("I do NOT have this email")
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

# def cleanAll(request):
#     x=book.objects.all()
#     x.delete()
#     x=author.objects.all()
#     x.delete()
#     return redirect('/')