def secondLargest(list1):
    list1.sort()
    ans=list1[-2]
    return ans
    
n=int(input("Enter no. of elements"))
l=[]
for i in range(n):
    l.append(int(input()))
print(secondLargest(l))    

