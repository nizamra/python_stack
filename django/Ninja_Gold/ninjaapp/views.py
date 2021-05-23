from django.shortcuts import redirect, render
import random
from time import gmtime, strftime, localtime

def index(request):
    request.session['GoldPlus']=0
    request.session['Activity']=[]
    return render(request,'index.html')
    
def index2(request):
    return render(request,'index2.html')

def howMuchGold(request):
    if request.POST['whereAmI']=="farm":
        request.session['GoldPlus']=random.randint(10,20)
        request.session['whereAmI'] = request.POST['whereAmI']
    elif request.POST['whereAmI']=="cave":
        request.session['GoldPlus']=random.randint(5,10)
        request.session['whereAmI'] = request.POST['whereAmI']
    elif request.POST['whereAmI']=="house":
        request.session['GoldPlus']=random.randint(2,5)
        request.session['whereAmI'] = request.POST['whereAmI']
    elif request.POST['whereAmI']=="casino":
        request.session['GoldPlus']=random.randint(-50,50)
        request.session['whereAmI'] = request.POST['whereAmI']
        if request.session['GoldPlus']<0:
            pass
        else:
            request.session['whereAmI'] = request.POST['whereAmI']
    
    request.session['Activity'].append(f"you earned {request.session['GoldPlus']} from {request.session['whereAmI']} exactly at {strftime('%Y-%m-%d %H:%M %p', localtime())}")
    context={
        'activities':request.session['Activity']
    }
    
    return render(request,'index.html', context)

def clarity(request):
    request.session.clear()
    return redirect('/')