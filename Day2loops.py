#Doing 2 tasks on loops

#Printing numbers using for
for i in range(10):
    print(f"{i+1}")

#Sum using while
initial=1
sum=0
a=int(input("THE NUMBER IS: "))
while initial<=a:
    sum=sum+initial
    initial+=1
print(f"{sum}")

#Greatest of three numbers
a,b,c=map(int,input("Enter three numbers separated by spaces: ").split())
print(f"The values of numbers are a={a},b={b} and c={c}")
maximum=max(a,b,c)
print(f"The maximum value is {maximum}")

#Multiplication table using for loop
num=int(input("The number for multiplication table is: "))
for count in range(10):
    multi=num*(count+1)
    print(f"{num} x {count+1} = {multi}")


#Counting vowels in string
# Taking input string from the user
user_input = input("Enter a string: ")

# Defining a set of vowels
vowels = 'aeiouAEIOU'

# Initializing a counter for vowels
vowel_count = 0

# Counting the number of vowels in the input string
for char in user_input:
    if char in vowels:
        vowel_count += 1

# Printing the number of vowels
print(f"The number of vowels in the string is: {vowel_count}")

try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("That's not a valid number!")

try:
    num1=int(input("Enter the divisor: "))
    div=10/num1
    print(f"The answer is : {div}")
except num1==0:
    print("That is an error")




