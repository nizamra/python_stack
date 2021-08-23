s="madamimadam"
# s="wesk"

# def answerQuery(l, r):
#     substring = s[l-1:r]
#     print(substring)
#     listing=list(substring)
#     print("Listing First",listing)
#     xx=len(listing)
#     print("length= ", xx)
#     sett=set()
#     for i in range(xx):
#         for j in range(1,xx):
#             print("Fuzzy First ",i,j,listing)
#             backk="".join(listing)
#             if (backk==backk[::-1]):
#                 print("Found One",backk)
#                 sett.add(backk)
#                 print("set",sett)
#             for sally in range(xx):
#                 if (backk[:-sally]==backk[:-sally][::-1]):
#                     print("something Here")
#                     print(backk[:-sally],backk[:-sally][::-1])
#                     sett.add(backk[:-sally])
#             listing[i],listing[j]=listing[j],listing[i]
#     list2=list(sett)
#     maxLen=len(max(list2, key=len))
#     print("settings hamburger",maxLen)
#     cnt=0
#     for string in list2:
#         if len(string)==maxLen:
#             cnt+=1
#     return cnt

def answerQuery(l, r):
    substring = s[l-1:r]
    listing=list(substring)
    xx=len(listing)
    sett=set()
    for i in range(xx):
        for j in range(1,xx):
            backk="".join(listing)
            if (backk==backk[::-1]):
                sett.add(backk)
            for sally in range(xx):
                if (backk[:-sally]==backk[:-sally][::-1]):
                    sett.add(backk[:-sally])
            listing[i],listing[j]=listing[j],listing[i]
    list2=list(sett)
    maxLen=len(max(list2, key=len))
    cnt=0
    for string in list2:
        if len(string)==maxLen:
            cnt+=1
    return cnt
print("Tamam",answerQuery(4,7))