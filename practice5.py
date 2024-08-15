#pattern problems
from email.contentmanager import raw_data_manager

for i in range(1,6): #rows
    for j in range(1,6): #cols
        print(j,end=" ")
    print()

#O/P:
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5


for i in range(1,6): #rows
    for j in range(1,i+1): #cols
        print(j,end=" ")
    print()

#O/P:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

for i in range(1,6): #rows
    for j in range(1,i+1): #cols
        print("*",end=" ")
    print()


#*
#* *
#* * *
#* * * *
#* * * * *

for i in range(1,6): #rows
    for j in range(1,i+1): #cols
        print(i,end=" ")
    print()

#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

for i in range(1,6): #rows
    for j in range(6,i,-1): #cols
        print(i,end=" ")
        #print("*", end=" ")
    print()

#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5

for i in range(1,6): #rows
    for j in range(5,i,-1): #cols
        print(" ",end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

#        *
#      * *
#    * * *
#  * * * *
#* * * * *

for i in range(1,6): #rows
    for j in range(i,0,-1): #cols
        print(j,end=" ")
        #print("*", end=" ")
    print()

#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1

for i in range(1,6): #rows
    for j in range(1,i+1): #cols
        print("*", end=" ")
    print()
for i in range(5,0,-1):
    for k in range(0, i - 1):  # cols
        print("*", end=" ")
    print()

#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=" ")
    print()

#1 2 3 4 5
#2 4 6 8 10
#3 6 9 12 15
#4 8 12 16 20
#5 10 15 20 25

for i in range(1,6):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()

#1
#2 4
#3 6 9
#4 8 12 16
#5 10 15 20 25