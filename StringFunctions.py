a="hello"
b="Hello123"
c="123456"
d="HELLO"
e=" "
f="Hello 123"
g="1.234"

#isalnum->Return True if all char in the string are alphanumeric
print(a,a.isalnum())   #a,b,c,d

#isalpha->Return True if all char in the string are in alphabet
print(b,b.isalpha()) #a,d

#isdecimal->Return True if all char in the string are in decimal
print(c,c.isdecimal()) #c

#isdigit->Return True if all char in the string are digits
print(c,c.isdigit()) #c

#isnumeric->Return True if all char in the string are numeric
print(c,c.isnumeric()) #c

#islower->check string is in lowercase
print(a,a.lower()) #a

#isupper->check string is in uppercase
print(d,d.upper()) #d

#isspace->Return True if all char in the string are whitespaces
print(e,e.isspace()) #e

#istitle->Return True if the string follows the rules of a title.
print(b,b.istitle()) #a,d,f


#Advanced string functions
#endswith()->Return true if the string ends with the specified value
y="Harry Potter"
print(y.endswith("r")) #True
print(y.endswith("P")) #false
print(y.endswith("y")) #false

#startswith()->Return true if the string starts with the specified value
print(y.startswith("H")) #True
print(y.startswith("P")) #false
print(y.startswith("P",6,9)) #True

#swapcase()->swaps cases,lower case becomes uppercase and vice versa
print(y.swapcase())  #hARRY pOTTER

#strip()->Used to trim spaces from string
z="    Harry Potter   " #Harry Potter
print(z.strip(" "))

#split()->seperate string with specified seperator and return list
m="#00FD#BRB#0MW#TB"
n="hello. my name is john. i am 23 years old"
print(m.split("#"))  #['', '00FD', 'BRB', '0MW', 'TB']
print(n.split(".")) #['hello', ' my name is john', ' i am 23 years old']

#ljust()->left shift
j="harry potter"
h=j.ljust(20,"*")
print(h,"is my first movie")  #harry potter******** is my first movie

#rjust->right shift
k="Harry potter"
z=k.rjust(20,"*")
print(z,"is my first movie") #********harry potter is my first movie

#replace()->replace specific value
print(k.replace("harry","Lisa"))   #Lisa potter

#rindex()->return last position of value found
print(k.rindex("potter")) #6

#rfind()
print(k.rfind("Harry")) #0
print(k.find("p",5,9))  #6

#Slicing of string->break string into small parts
z="Harry potter and Goblet of fire"
print(z[0:5]) #Harry
print(z[6:12]) #potter
print(z[:5]) #Harry
print(z[-4:]) #fire
#reverse string
print(z[::-1])  #erif fo telboG dna rettop yrraH


s="0123456789"
print(s[::2]) #02468
print(s[:7:2]) #0246
#reverse numbers
print(s[::-1]) #9876543210
print(s[6::-1]) #6543210





