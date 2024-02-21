#Write a program to find a fibonacci of a number.

def fibonacci(n):
    a,b=0,1
    counter=0
    print(a)
    print(b)
    while(counter<=n):
        c=a+b
        print(c)
        a=b
        b=c
        counter+=1
input=int(input())
fibonnaci(input)
