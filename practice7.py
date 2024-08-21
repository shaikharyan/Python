#String Problems

a="OOTD.YOLO.ASAP.BRB.GTG.OTW"

#write a program to separate the following string into comma
b=a.split(".")
print(b)

# ['OOTD', 'YOLO', 'ASAP', 'BRB', 'GTG', 'OTW']


#write a program to sort string alphabetically
c=input("enter word: ")
d=sorted(c)
print(d)

#['e', 'h', 'l', 'l', 'o']


#write a program to remove a given character from string
e="hello"
f=e.replace("e","")
print(f)

#hllo


#write a program to remove dot from the string
h=a.replace(".","")
print(h)

#OOTDYOLOASAPBRBGTGOTW


#write a program to check the number of occurrence of substring in the string
x="she sells seashells on the sea shore"
y=x.count("sea")
print("the number of times sea is occuring:",y)

#the number of times sea is occuring: 2