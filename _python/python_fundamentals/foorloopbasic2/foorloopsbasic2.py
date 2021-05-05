def func(list):
    for i in range(4):
        if(list[i]>0):
            list[i]="biggie"
    return list
print(func([-5,1,2,-3]))

def func(list):
    sum=0
    for i in range(len(list)):
        if(list[i]>0):
            sum=sum+1
    list.pop()
    list.append(sum)
    return list
print(func([1,2,3,4,-2]))

def func(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum
print(func([1,2,3,4,5]))    

def func(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum/len(list)
print(func([1,2,3,4,5]))    

def func(list):
    return len(list)
print(func([1,2,3,4,5]))    

def func(list):
    min=list[0]
    if not list:
        return False
    else:
        for i in range(1,len(list)):
            if(list[i]<min):
                min=list[i]
    return min
print(func([1,2,-5,4,5]))    

def func(list):
    max=list[0]
    if not list:
        return False
    else:
        for i in range(1,len(list)):
            if(list[i]>max):
                max=list[i]
    return max
print(func([1,2,-5,4,5]))    

def func(list):
    max=list[0]
    min=list[0]
    sum=0
    newlist=[]
    if not list:
        return False
    else:
        for i in range(1,len(list)):
            sum+=list[i]
            if(list[i]>max):
                max=list[i]
            if(list[i]<min):
                min=list[i]
    avg=sum/len(list)
    newlist.append("max is: {}".format(max))
    newlist.append("min is: {}".format(min))
    newlist.append("sum is: {}".format(sum))
    newlist.append("avg is: {}".format(avg))
    return newlist
print(func([1,2,-5,4,5]))    

def func(list):
    lens=len(list)+1
    for i in range(0,lens):
        list.insert(0,list[i+i-1])
    for i in range(6):
        list.pop()
    return list
print(func([1,2,3,4,5]))