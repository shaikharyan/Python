#functions

#write a function to find maximum of three numbers in python
def maximum(a,b,c):
    if a>b and a>c:
        print(a,"is the maximum")
    elif b>a and b>c:
        print(b,"Is the maximum")
    else:
        print(c,"is the maximum")

maximum(2,5,8)  #8 is the maximum
maximum(12,5,8) #12 is the maximum

#write a python function to create and print a list where the values are square of numbers between 1 and 30.
def create_list():
    l=[]
    for i in range(1,31):
        l.append((i**2))

    return l

print(create_list())

#write a function that takes a number as a parameter and check if the number is prime or not.
def check_prime(num):
    if num==1:
        print("it is not prime")
    if num==2:
        print("it is not prime")
    for i in range(2,num):
        if num%i==0:
            print("it is not prime")
            break
    else:
        print("it is prime")
check_prime(34) #it is not prime
check_prime(31) #it is prime

#write a function to sum all the numbers in a list.
def add(num):
    total=0
    for i in num:
        total=total+i
    return total
print(add([12,4,5,6,7,8]))  #42

#write a program to solve the fibonacci series using recursion.
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fib(n-1)+(n-2))

print(fib(7))  #16