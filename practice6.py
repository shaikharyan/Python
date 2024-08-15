#write a program to get fibonacci series upto 10 numbers.
a=0
b=1
n=int(input("Enter number: "))
if n==1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c,end=" ")


#Enter number: 13
#0
#1
#1 2 3 5 8 13 21 34 55 89 144


#write a number to check if a number is prime or not
num=int(input("enter number here: "))
if num<=1:
    print("it is not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("number is not a prime number")
            break
    else:
            print("it is a prime number")

#enter number here: 12
#number is not a prime number

#enter number here: 7
#it is a prime number

#write a program to find a palindrome of integers.
num=int(input("enter number here: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = (reverse * 10) + digit
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")

#enter number here: 1221
#Palindrome