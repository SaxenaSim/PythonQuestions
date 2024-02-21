def removeDuplicates(numbers):
    uniqueNumbers = []
    for i in numbers:
        if i not in uniqueNumbers:
            uniqueNumbers.append(i)
    return uniqueNumbers

n=int(input("Enter no. of elements"))
l=[]
for i in range(n):
    l.append(int(input())
uniqueNums = removeDuplicates(l)
for i in range(len(uniqueNums)):
    print(uniqueNums[i])
