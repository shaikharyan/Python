for i in range(1,6):
    print(i)  #1 2 3 4 5

#print odd
for i in range(1, 6,2):
    print(i)  # 1 3 5

#print table
n=5
for i in range(1,11):
    print(n,"x",i,"=",n*i)

#while loop
#print counting
n=0
while n<=5:
    print(n)
    n+=1

#print 7 table
n=1
a=7
while n<=10:
    print(a,"x",n,"=",n*a)
    n+=1

#while true->infinite loop to stop break statement is used.
while True:
    print("hello")
    break

#nested loop
for i in range(1,4):
    for j in range(1,11):
        #print(j)
        #if want to print in single line
        print(j, end="")
    print()


#pattern
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


#eg.1
for i in range(1,11):
    if i==3:
        print("add")
    else:
        print(i)

#eg.2:common number in both table
for i in range(1,101):
    if i%8==0 and i%12==0:
        print(i)  #24 48 72 96


#eg.1
n=1
while n<=10:
    if n==3:
        print("add")
    else:
        print(n) #1 2 add 3 4 5 6 7 8 9 10
    n+=1


#continue->skip
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i)   #1 2 3 4 6 7 8 9 10

#break
for i in range(1,11):
    if i==7:
        break
    else:
        print(i)  #1 2 3 4 5 6