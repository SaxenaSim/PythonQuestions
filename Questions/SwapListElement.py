def swapList(l1):
    size=len(l1)
    temp=l1[0]
    l1[0]=l1[size-1]
    l1[size-1]=temp
    return l1
    
newList=[12,23,34,56,67,78]
l2=swapList(newList)
for i in l2:
    print(i)
