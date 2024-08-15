x="hello"
print(x)
print(type(x))

a="harry Potter and the Goblet of Fire"
print(a)

#lenght of string
print(len(a)) #35

#count of e character
print(a.count("e")) #4

#lowercase
print(a.lower()) #harry potter and the goblet of fire

#uppercase
print(a.upper()) #HARRY POTTER AND THE GOBLET OF FIRE

#to find index of any character
#print(a.index("o")) #7
print(a.index("o",15,34)) #22

#capitalize->convert first letter of alphbet into uppercase
print(a.capitalize()) #Harry potter and the goblet of fire

#casefold->convert first letter of alphabet into lower
print(a.casefold()) #harry potter and the goblet of fire

#find->
print(a.find("o")) #7
print(a.find("o",15,34)) #22

#format
name="John"
age=22
b="my name is {}. and my age is {}"
print(b.format(name,age))  #my name is John. and my age is 22


#center
print(name.center(20,"*"))
#********John********