try:
    num1=int(input("Enter the divisor: "))
    div=10/num1
    print(f"The answer is : {div}")
except ZeroDivisionError:
    print("Cant Divide by 0!!!")

# Write a program to categorize a person based on age and employment status.

age=int(input("Type your age: "))
def get_user_input():
    while True:
        user_input=input("Enter the employment status('Y'=yes and 'N'=no) : ")
        if user_input=='Y':
            print("You have selected Yes")
            break
        elif user_input=='N':
            print("You have selected No")
            break
        else:
            print("Invalid Input: Please type Y for yes and N for no")
            
    return user_input

emp=get_user_input()
print("Status: ")
if age<0:
    print(f"Still a sperm, Idiot!")
elif age<18:
    if emp=='Y':
        print(f"Minor and Employed")
    else:
        print(f"Minor and Unemployed")
elif age<60:
    if emp=='N':
        print(f"Adult and Unemployed")
    else:
        print(f"Adult and Employed")
else:
    if emp=='Y':
        print(f"Senior Citizen and Retarded")
    else:
        print(f"Senior Citizen and Retired")


#Create a decision-making program that recommends a meal based on the time of day and dietary preferences.

