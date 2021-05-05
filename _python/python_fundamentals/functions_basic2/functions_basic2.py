def func(num):
    arr=[]
    for i in range(num,-1,-1):
        arr.append(i)
    print(arr)

func(5)

def func(arr):
    print(arr[0])
    return arr[1]
func([1,2])

def func(list):
    return list[0]+len(list)
print(func([1,2,3]))

def func(list):
    newlist=[]
    for i in range(0,len(list),1):
        if(list[i]>list[1]):
            newlist.append(list[i])
    return newlist
print(func([1,2,3,4]))

def func(list):
    newlist=[]
    for i in range (0,list[0],1):
        newlist.append(list[1])
    return newlist
print(func([6,2]))