'''
1.Write a program to exhibit these concepts:
    i. try
    ii. except
    iii. finally
'''
try:
    num=int(input('Enter an integer: '))
    print(num)
except:
    print("This is not a valid integer")
finally:
    print('End Of Program')


'''
2.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
'''
try:
    num1=int(input("Enter the numerator: "))
    num2=int(input("Enter the denominator: "))
    if num2==0:
        raise ZeroDivisionError("Can't Divide by Zero")
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Entered num are not integer")
else:
    print(num1/num2)


'''
3.Write a Python program that prompts the user to input an integer and 
  raises a ValueError exception if the input is not a valid integer.
'''
try:
    num=int(input("Enter an integer: "))
except ValueError:
    print("Entered number is not an integer")
else:
    print("The entered integer is :",num)


'''
4.WAP that exhibits multiple except blocks along with default block
'''
try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    result=num1 / num2 
except ValueError:
    print("Invalid input: Please enter integers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result of {num1} divided by {num2} is {result}")


'''
5.WAP that exhibits except blocks that can catch multiple exceptions.
'''
try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    result=num1 / num2
        
except (ValueError, TypeError) as e:
    print("Invalid input: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"The result of {num1} divided by {num2} is {result}")

