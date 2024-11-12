# class students: 
#     listroll=[]
#     listname=[]
#     def __init__(self,roll,name):
#         students.listroll.append(roll)
#         students.listname.append(name)
#     def display(self):
#         print(students.listroll)
#         print(students.listname)
# s1=students(1,'siva')
# s2=students(2,'sivaa')
# s3=students(3,'sivaaa')
# s4=students(4,'sivaaaa')
# s5=students(5,'sivaaaaa')
# s5.display()


# # 6. Write a Python class Employee with attributes like emp_id, emp_name,
# # emp_salary, and emp_department and methods like
# # calculate_emp_salary, emp_assign_department, and print_employee_details. 
# # (More data was there but did not write - question too big)

# class employee:
#     id=[]
#     names=[]
#     salary=[]
#     overtime=[]
#     otamt=[]
#     dep=[]
#     def emp_id(self,empid):
#         employee.id.append(empid)
#     def emp_name(self,name):
#         employee.names.append(name)
#     def emp_salary(self,sal,hour):
#         employee.salary.append(sal)
#         ot=hour-50
#         employee.overtime.append(ot)
#         amt=ot*(sal/50)
#         employee.otamt.append(amt)
#     def emp_department(self,depar):
#         employee.dep.append(depar)
#     def print_details(self):
#         print(employee.id)
#         print(employee.names)
#         print(employee.salary)
#         print(employee.overtime)
#         print(employee.otamt)
#         print(employee.dep)
# a=employee()
# j=employee()
# m=employee()
# s=employee()
# a.emp_id('E7876')
# a.emp_name('ADAMS')
# a.emp_salary(50000,50)
# a.emp_department('ACCOUNTING')
# j.emp_id('E7499')
# j.emp_name('JONES')
# j.emp_salary(45000,50)
# j.emp_department('RESEARCH')
# m.emp_id('E7900')
# m.emp_name('MARTIN')
# m.emp_salary(50000,50)
# m.emp_department('SALES')
# s.emp_id('E7698')
# s.emp_name('SMITH')
# s.emp_salary(55000,55)
# s.emp_department('OPERATIONS')
# s.print_details()

# class shopping:
#     shop_list={}
#     def add_item(self):
#         l=[]
#         while True:
#             self.itemlist=input("Enter the item and price seperated by a space (say end to stop): ")
#             if self.itemlist!='end':
#                 self.itemlist=self.itemlist.split()
#                 l.append(self.itemlist)
#                 dict(l)
#                 self.shop_list.update(l)
#             elif self.itemlist=='end':
#                 break
#         print(self.shop_list)
#     def remove_item(self):
#         while True:
#             n=input("Enter the item you want to remove (say no to stop): ")
#             if n in self.shop_list.keys() and n!='no':
#                 self.shop_list.pop(n)
#             elif n=='no':
#                 break
#             print(self.shop_list)
#     def add_total(self):
#         total=0
#         for i in self.shop_list.values():
#             i=int(i)
#             total=total+i
#         print('The cost of the items is :',total,'Rupees')


'''
s = lambda a: a*a
x=s(4)
print(x)


add = lambda a,b: a+b
x=add(4,5)
print(x)



def reciprocal( num ):  
    return 1 / num  
   
lambda_reciprocal = lambda num: 1 / num  
   
# using the function defined by def keyword  
print( "Def keyword: ", reciprocal(6))  
   
# using the function defined by lambda keyword  
print( "Lambda keyword: ", lambda_reciprocal(6))  



# Code to use lambda function with if-else    
Minimum = lambda x, y : x if (x < y) else y       
print('The greater number is:', Minimum( 35, 74 ))


items_cost = [999, 888, 1100, 1200, 1300, 777]
gt_thousand = filter(lambda x : x>1000, items_cost)
x=list(gt_thousand)
print("Eligible for discount: ",x)


without_gst_cost = [100, 200, 300, 400]
with_gst_cost = map(lambda x: x+10, without_gst_cost)
x=list(with_gst_cost)
print("Without GST items costs: ",without_gst_cost)
print("With GST items costs: ",x)


from functools import reduce
each_items_costs = [111, 222, 333, 444]
total_cost = reduce(lambda x, y: x+y, each_items_costs)
print(total_cost)


import functools
lis = [1, 3, 5, 6, 2, 4]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))



List = [[2,4,3],[1, 64, 16, 4],[12, 9, 3, 6]]

sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y)-1] for y in f(x)]
res = secondLargest(List, sortList)

print(List)
print(res)


#-----------------------------------------------------------------

def add(x):            
    return x+1         
def sub(x):            
    return x-1

def operator(func, x):      
    temp = func(x)    
    return temp    

print(operator(sub,10))    
print(operator(add,20))  




def decor(func):
   def inner_function(x,y):
       if x<0:
           x = 0
       if y<0:
           y = 0
       return func(x,y)
   return inner_function 

def add(a,b):
   res = a + b
   return res

add = decor(add)
print(add(20,30))
print(add(-10,5))





def decor(func):
   def inner_function(x,y):
       if x<0:
           x = 0
       if y<0:
           y = 0
       return func(x,y)
   return inner_function 

@decor
def sub(a,b):
   res = a - b
   return res

print(sub(30,20))
print(sub(10,-5))


#-----------------------------------------------------------------


def get_odds_generator():
    n=1
    
    n+=2
    yield n
    
    n+=2
    yield n 
    
    n+=2
    yield n
    
numbers=get_odds_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))


def m():
   yield 'Mahesh'
   yield 'Suresh'

g = m()
print(g)
print(type(g))
for y in g:
   print(y)

'''


'''
def m(x, y):
   while x<=y:
       yield x
       x+=1

g = m(5, 10)
for y in g:
   print(y)
'''



'''
def m():
   yield 'Mahesh'
   yield 'Suresh'
g = m()

print(type(g))
print(next(g))
print(next(g))
'''



'''
# 1) Demonstrate arithmetic operators

a = 10
b = 5
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print(f"Floor Division: {a // b}")

# 2) Find the greatest number among three numbers

def greatest_number(a, b, c):
return max(a, b, c)
print("Greatest number:", greatest_number(10, 25, 15))

# 3) Add numbers from 5 to 15 using for loop

total = 0
for i in range(5, 16):
total += i
print("Sum of numbers from 5 to 15:", total)

# 4) Find factorial of a number

def factorial(n):
if n == 0 or n == 1:
return 1
else:
return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

# 5) Print the following patterns

for i in range(1, 6):
print('* ' * i)

# 6) Calculate sum and average of a given array

arr = [1, 2, 3, 4, 5]
sum_arr = sum(arr)
avg_arr = sum_arr / len(arr)
print(f"Sum: {sum_arr}, Average: {avg_arr}")

# 7) Check whether a number is prime or not

def is_prime(n):
if n < 2:
return False
for i in range(2, int(n**0.5) + 1):
if n % i == 0:
return False
return True
print("Is 11 prime?", is_prime(11))

# 8) Recursive function to print Fibonacci series up to 10 terms

def fibonacci(n):
if n <= 1:
return n
else:
return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(10):
print(fibonacci(i), end=" ")
print("\n")

# 9) Check whether a string is palindrome or not

def is_palindrome(s):
return s == s[::-1]
print("Is 'madam' palindrome?", is_palindrome("madam"))

# 10) Calculate sum of variable number of arguments

def sum_of_args(*args):
return sum(args)
print("Sum of 1, 2, 3:", sum_of_args(1, 2, 3))

# 11) Remove duplicates from a list

arr_with_duplicates = [1, 2, 2, 3, 4, 4]
unique_arr = list(set(arr_with_duplicates))
print("Unique items:", unique_arr)

# 12) Calculate square of numbers from 1 to 10 using list comprehension

squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)

# 13) Element-wise sum of given tuples

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)
elementwise_sum = tuple(a + b + c for a, b, c in zip(tuple1, tuple2, tuple3))
print("Element-wise sum:", elementwise_sum)

# 14) Get only unique items from two sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
unique_items = set1.union(set2)
print("Unique items from both sets:", unique_items)

# 15) Dictionary comprehension for even age

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_age_dict = {key: value for key, value in original_dict.items() if value % 2 == 0}
print("Dictionary with even age:", even_age_dict)

# 16) Remove spaces from a given string

string = "Python is very easy"
no_spaces = string.replace(" ", "")
print("String without spaces:", no_spaces)

# 17) Calculate simple interest

principle_amount = float(input("Enter principle amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
simple_interest = (principle_amount * rate * time) / 100
print(f"Simple Interest: {simple_interest:.2f}")

# 18) Circle class with area and perimeter

import math
class Circle:
def **init**(self, radius):
self.radius = radius
def area(self):
return math.pi * self.radius ** 2
def perimeter(self):
return 2 * math.pi * self.radius
circle = Circle(5)
print(f"Area of Circle: {circle.area():.2f}")
print(f"Perimeter of Circle: {circle.perimeter():.2f}")

# 19) Person and Student class with inheritance

class Person:
def **init**(self, name, age):
[self.name](http://self.name/) = name
self.age = age
class Student(Person):
def **init**(self, name, age, rollno, stream):
super().**init**(name, age)
self.rollno = rollno
self.stream = stream
def display(self):
print(f"Name: {[self.name](http://self.name/)}, Age: {self.age}, Roll No: {self.rollno}, Stream: {self.stream}")
student = Student("John", 20, "1234", "Science")
student.display()

# 20) Count number of words in a text file

filename = "text_file.txt"
with open(filename, 'r') as file:
content = file.read()
word_count = len(content.split())
print(f"Number of words in the file: {word_count}")

# 21) Handle ZeroDivisionError

try:
num1 = 10
num2 = 0
result = num1 / num2
except ZeroDivisionError:
print("Error: Division by zero is not allowed.")

# 22) Lambda in map() function

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)

# 23) Lambda in filter() function

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 24) Class method and static method demonstration

class Demo:
@classmethod
def class_method(cls):
print("This is a class method")
@staticmethod
def static_method():
print("This is a static method")
Demo.class_method()
Demo.static_method()

# 25) GUI application to add two numbers

import tkinter as tk
def add_numbers():
result = float(entry1.get()) + float(entry2.get())
label_result.config(text=f"Result: {result}")
root = [tk.Tk](http://tk.tk/)()
root.title("Add Two Numbers")
label1 = tk.Label(root, text="Enter number 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
label2 = tk.Label(root, text="Enter number 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
button = tk.Button(root, text="Add", command=add_numbers)
button.pack()
label_result = tk.Label(root, text="Result:")
label_result.pack()
root.mainloop()
'''




'''
import tkinter

# note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()


from tkinter import *
root = Tk()
w = Label(root, text='B.Tech CSE',fg='red')
w.pack()
root.mainloop()


import tkinter as tk

r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()



from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack(side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()




from tkinter import *


def getCheckValue1():
    print(CheckVar1.get())


top =Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1,onvalue = 1,offvalue = 0,height=5,width = 20,
                 command=getCheckValue1)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2,onvalue = 1,offvalue = 0,height=5, width = 20)
C1.pack()
C2.pack()

top.mainloop()




'''

# from tkinter import *

# from tkinter import messagebox


# top = Tk()
# top.geometry("200x200")
# def hello():
#     num1 = float(E1.get())
#     num2 = float(E2.get())
#     result = num1 + num2
#     messagebox.showwarning("Say Hello", result)

# E1 = Entry(top, bd =5)
# E1.pack()

# E2=Entry(top, bd =5)
# E2.pack()



# B1 = Button(top, text = "Say Hello", command = hello,font=("family=Helvetica,size=36,weight=bold"))
# B1.pack()

# top.mainloop()

'''

from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
R1.pack()

R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack()

R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
R3.pack()

label = Label(root)
label.pack()
root.mainloop()


from tkinter import * 

top = Tk()
B1 = Button(top, text ="FLAT", relief=FLAT )
B2 = Button(top, text ="RAISED", relief=RAISED )
B3 = Button(top, text ="SUNKEN", relief=SUNKEN )
B4 = Button(top, text ="GROOVE", relief=GROOVE )
B5 = Button(top, text ="RIDGE", relief=RIDGE )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()


'''
# from tkinter import *
# import tkinter
# top = Tk()

# B1 = Button(top, text ="error", relief=RAISED,bitmap="error",cursor="circle")
# B2 = Button(top, text ="hourglass", relief=RAISED,bitmap="hourglass",cursor="plus")
# B3 = Button(top, text ="info", relief=RAISED,bitmap="info")
# B4 = Button(top, text ="question", relief=RAISED,bitmap="question")
# B5 = Button(top, text ="warning", relief=RAISED,bitmap="warning")

# B1.pack()
# B2.pack()
# B3.pack()
# B4.pack()
# B5.pack()
# top.mainloop()

# str='snow ball'
# str[3]='s'
# print(str)
# class Demo:
#     @classmethod
#     def class_method(cls):
#         print("This is a class method")
#     @staticmethod
#     def static_method():
#         print("This is a static method")
# Demo.class_method()
# Demo.static_method()
import tkinter as tk
def add_numbers():
    result = float(entry1.get()) + float(entry2.get())
    label_result.config(text=f"Result: {result}")
root = tk.Tk()
root.title("Add Two Numbers")
label1 = tk.Label(root, text="Enter number 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
label2 = tk.Label(root, text="Enter number 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
button = tk.Button(root, text="Add", command=add_numbers)
button.pack()
label_result = tk.Label(root, text="Result:")
label_result.pack()
root.mainloop()