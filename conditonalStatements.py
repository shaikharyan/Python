marks=87
if marks>=90:
    print("A")
print("thank you")  #



if marks>=50:
    print("Pass")  #
else:
    print("Fail")


if marks>=80:
    print("A")
elif marks>=60:
    print("B")
elif marks>=50:
    print("C")
else:
    print("Fail")

#Nested condition
if marks>=80:
    print("Won")
    if marks>=90:
        print("go to trip")
else:
    print("Nothing")

#short hand if statement
if marks>=80: print("Won")

#short hand if else statement
print("Won") if marks>=90 else print("Fail")