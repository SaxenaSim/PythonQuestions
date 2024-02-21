def findCommonElements(list1, list2):
    commonElements = []
    for item in list1:
        if item in list2:
            commonElements.append(item)
    return commonElements
    
n=int(input("enter no. of elements"))
list1=[]
list2[]
for i in range(n):
    list1.append(int(input()))
for i in range(n):
    list2.append(int(input()))
common = findCommonElements(list1, list2)
for i in common:
    print(i)
