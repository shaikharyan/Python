#write a program to check a number is postive or not
from random import choice


num=int(input("Enter the number"))
if num>0:
    print("positive") #
else:
    print("Negative")

#write a program to check whether a vowel or not
letter=input("Enter letter ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is vowel")
else:
    print("it is not vowel")

#write a program to check a number is odd or even
if num%2==0:
    print("even") #
else:
    print("odd")


#write a program to create area calculator

print("Area Calculator")
print("""press 1 to get area of sqaure
press 2 to get area of rectangle
press 3 to get area of circle
press 4 to get area of triangle""")

choice=int(input("Enter the choice"))
if choice==1:
    side=float(input("Enter length of one side"))
    area=side*side
    print("area is: ",area)
elif choice==2:
    length=float(input("Enter length"))
    width=float(input("Enter width"))
    area=length*width
    print("area is: ",area)
elif choice==3:
    radius=float(input("Enter radius"))
    area=3.14*(radius**2)
    print("area is: ",area)
elif choice==4:
    base=float(input("Enter base"))
    height=float(input("Enter height"))
    area=0.5*base*height
    print("area is: ",area)
else:
    print("Invalid input")