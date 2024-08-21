#loops
#write a program to find a sum of all the even number upto 50

sum=0
for i in range(1,51):
    if i%2==0:
        sum+=i
print("The sum is: ",sum)  #650


#write a program to write first 20 numbers and their square numbers

for i in range(1,21):
    print(i,i**2)

#write a program to find sum of first 10 odd numbers using while loop

sum=0
i=0
while i<=20:
    if i%2!=0:
        sum+=i
    i+=1
print("sum is: ",sum) #100


#write a program to check if a number is divisible by 8 and 12 utp 100 numbers

for i in range(1,101):
    if i%8==0 and i%12==0:
        print(i) #24 48 72 96

#Write a program to create a billing system in supermarket
while True:
    name=input("Enter customer name: ")
    total=0

    while True:
        print("enter the amount and quantity")
        amount=float(input("Enter amount "))
        quantity=float(input("Enter quantity: "))
        total+=amount*quantity
        repeat=input("do you want to add more items?(yes/no):")
        if repeat=="no" or repeat=="No":
            break
    print("-"*40)
    print("Name: ",name)
    print("Amount: ",total)
    print(("-"*40))
    print("******HAPPY SHOPPING ******")
    repeat1=input("do you want to go next customer?(yes/no): ")
    if repeat1 == "no" or repeat1 == "No":
        break





