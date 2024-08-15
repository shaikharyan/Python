#Take an input from user as a string then reverse it.
a=input("Enter string here: ")
print(a[::-1])  #olleh

#write a program to check if a string contains only digits.
c=input("Enter string here: ")
b=(c.isdigit())
if b==True:
    print("is contains only digits")
else:
    print("it does not contain digit")

#Enter string here: 123
#is contains only digits

#write a program to find number of vowels in a string
d=input("Enter here: ")
vowels=0
for i in d:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vowels+=1
print("vowels is:",vowels)

#Enter here: hello
#vowels is: 2

#write a program to check if every word in a string begins with a capital letter.
e=input("Enter here: ")
print(e.istitle())

#Enter here: Hello How Yow Are
#True