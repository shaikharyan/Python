a=[30,40,50,60]

b=[]
for i in a:
    b.append(i)

print(a,"\n",b)

#O/P:
#[30, 40, 50, 60]
#[30, 40, 50, 60]

c=[]
for i in a:
    if i>45:
     c.append(i)

print(a,"\n",c)

#O/P:
#[30, 40, 50, 60]
#[50, 60]

#list comprehension
l3=[i for i in a]
print(l3) #[30, 40, 50, 60]

l3=[i for i in a if i >45]
print(l3) #[50, 60]


