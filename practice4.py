#string problems
a="Why fit in,When you are Born to Stand Out!"

#write a program to find the lenght of the following string
b=(len(a))
print("Lenght of a string is" ,b)  #42

#write a program to check how many time alphabet o is occuring.
print(a.count("o")) #3

#write a program to convert the whole string into lower and upper classes
x=a.lower()
print(x) #why fit in,when you are born to stand out!
y=a.upper()
print(y)  #WHY FIT IN,WHEN YOU ARE BORN TO STAND OUT!

#write a program to convert the following string into a title
z=a.title()
print(z)  #Why Fit In,When You Are Born To Stand Out!

#write a program to find the index number of "fit in".
print(a.find("fit in"))  #4