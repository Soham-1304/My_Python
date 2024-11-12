#Today we learn loops and conditional statements

print("Today we learn loops")
#Code to check sign of number

a=int(input("The number to check is:"))
if a==0:
    print("The given number is Zero")
elif a>0:
    print("The given number is Positive")
else:
    print("The given number is Negative")

#Code to check leap year
b=int(input("Enter the Year you want to check:"))
if b%4==0:
    print("The given year is a Leap Year")
else:
    print("The year is Not a Leap Year")
