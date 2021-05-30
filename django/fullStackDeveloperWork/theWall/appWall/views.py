from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    try:
        allPosts = Post.objects.all()
        context={
        'allPosts' : allPosts
        }
        return render(request,'index.html', context)
    except:
        return render(request,'index.html')

def deletingPost(request , postId):
    deletedPost=Post.objects.get(is=postId)
    deletedPost.delete()
    deletedPost.save()
    return redirect('/')

def methodAddingPost(request):
    if (request.method=="POST") and (request.POST['someForm']=="newPost"):
        thisPost=request.POST['postInForm']
        thisPostsCreator=request.POST['creator']
        errors = Post.objects.postIsValid(thisPost)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            Post.objects.create(post=thisPost,createdBy=thisPostsCreator)
            return redirect('/')

def cleanTheSession(request):
    request.session.clear()
    return redirect('/')