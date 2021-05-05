import random
def randInt(min=0   , max=100  ):
    if(min>max):
        return "min cannot be bigger than max"
    if(max<0):
        return "max cannot be smaller than zero"
    num =min+ random.random()*max
    return num
print(randInt(0,50))