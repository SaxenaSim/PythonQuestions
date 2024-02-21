def numberIsPalindrome(a):
        temp=a
        reverse=0
        while(temp>0):
            remainder=temp%10
            reverse=(reverse*10)+remainder
            temp=temp//10
        if(a==reverse):
            return "Number is Palindrome"
        else:
            return "Number is not a palindrome"
            
input = int(input("Enter a number"))
print(numberIsPalindrome(input))
