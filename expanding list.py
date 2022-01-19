#question1 expanding list
def expanding(lst):
     list1=[]
    for i in range(1, len(lst)):
        s = lst[i]-lst[i-1]
        list1.append(abs(s))
    a= True
    for j in range(1, len(list1)):
        if list1[j]<=list1[j-1]:
            a = False
            break

    return a

lst = list(map(int,input().split()))
print(expanding(lst))
