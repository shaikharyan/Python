a=("Oneplus","Nokia","Redmi")
print("Before ",type(a)) #Before  <class 'tuple'>
a=list(a)
print("after ",type(a)) #after  <class 'list'>

a.append("Vivo")
print(a) #['Oneplus', 'Nokia', 'Redmi', 'Vivo']
#convert list into tuple
a=tuple(a)
print(type(a)) #<class 'tuple'>
print(a)  #('Oneplus', 'Nokia', 'Redmi', 'Vivo')


#tuple functions
print("The count of Redmi is ",a.count(("Redmi"))) #1
print("The index of Nokia is ",a.index("Nokia")) #1

