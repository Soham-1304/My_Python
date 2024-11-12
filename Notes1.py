'''
Principle=8000
time=8   #In years
rate=5   #In percentage
simint=time*rate*Principle/100
print("The simple interst is: ",simint)
'''

'''
str='computer science'
str2='science'
print('str-',str)
print('str[0]-',str[0])
print('str[1:5]-',str[1:5])
print('str[3:]-',str[3:])
print('str[:3]-',str[:3])
print('str[:-1]-',str[:-1])
print('str[-1:]-',str[-1:])
print('str[1:7:2]-',str[-1:7:-2]) #[start:end:skip]
print(str*3)

for i in str2:
  print(i)

boo=str2.isupper()  # isupper() used to check if capital letter is there
print(boo)

marks=35
print(bool(marks>=55))

s1=[101,'amit',387273]
print(s1)
print(s1[1])
print(s1[2])
print(s1[0])

tup=(12,'amti',31131)
print(tup[0])
print(tup[1])
print(tup[2])

s1[1]='amol'
print(s1[1])

set1={11,22,33,22}
print(set1)

dict1={'roolll':093,'name':'soham','contact':3123121312}
print(dict1['roolll'])


print(type(s1))
print(type(dict1))
print(type(set1))
'''

'''fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

a="python"
b="is"
c="awesome"
print(a,b,c)
print(a+b+c)
'''
# x = "awesome"

# def myfunc():
#   global x
#   x="fantastic"
#   print("Python is " +x)

# myfunc()
# print("Python is "+x)

# g=27e4
# h=23.7E5
# print(g,h)
# name,code,ctc=input('Enter employee name,Employee code and CTC seperated by a space: ').split()
# print(name)
# print(code)
# print(ctc)

# Accept email id from user and give me username,and domain
# name,dom=input('Write your email here: ').split('@')
# print('\nThe Email is',name+dom)
# print('\nUsename is :',name)
# print('\nDomain name is:',dom)

# per=float(input("Enter your percentage: "))
# if(per>=90 and per<=100):
#     print("Merit")
# elif(per>=75 and per<90):
#     print("Distinction")
# elif(per>=60 and per<75):
#     print("First Class")
# elif(per>=45 and per<60):
#     print("Second Class")
# elif(per>=35 and per<45):
#     print("Pass")
# elif(per>=0 and per<35):
#     print("Fail")
# else:
#     print("Invalid Percentage, Guess you failed math atleast")

#User will enter month number and print no.of days

# month=int(input("Enter the month number (from 1-12): "))
# if(month==1):
#     print("January: Has 31 days")
# elif(month==2):
#     print("February: Has 28 days")
# elif(month==3):
#     print("March: Has 31 days")
# elif(month==4):
#     print("April: Has 30 days")
# elif(month==5):
#     print("May: Has 31 days")
# elif(month==6):
#     print("June: Has 30 days")
# elif(month==7):
#     print("July: Has 31 days")
# elif(month==8):
#     print("August: Has 31 days")
# elif(month==9):
#     print("September: Has 30 days")
# elif(month==10):
#     print("October: Has 31 days")
# elif(month==11):
#     print("November: Has 30 days")
# elif(month==12):
#     print("December: Has 31 days")


#OR

# mon=int(input("Enter month number: "))
# if(mon==1 or mon==3 or mon==5 or mon==7 or mon==8 or mon==10 or mon==12):
#     print("The month has 31 days")
# elif(mon==4 or mon==6 or mon==9 or mon==11):
#     print("The month has 30 days")
# else:
#     print("The month has 28 days")

# import array as np
# inp=(input("Enter numbers: "))
# lis=inp.split()
# print(lis)
# lis=[int(i) for i in lis]
# a=np.array('i',lis)
# print(a)

'''
open_file=open('abc.txt','w')
string="Piyush"
print(string, file=open_file)
open_file.close()

import time
print('Please enter your email-id:',end='',flush=True)
time.sleep(10)
'''

# a=2
# b='ITM'
# print("{0} is an integer while {1} is a string".format(a,b))

# print('This {Food} is {Adjective}.'.format(Food='VadaPav',Adjective='Tasty'))

# print("%d is an integer while %s is a string"%(a,b))

# pi=3.14159265359
# print('The value of pi is approx %.5f .'%pi)

# i=10 # counter initialization
# while i>=1: #condition -step2
#     print(i,end="  ")  # loop body -step 3
#     i-=1   #Increment -step 4- goto step 2 until i<=10
# print(" \nEnd of Loop!")

# c=int(input("Enter the number upto which you need natural no.s: "))
# for c in range(1,c+1,3):
#     print(c,end=" ")
# print("\nEnd of Loop")

# for i in range(10,0,-1):
#     print(i,end=" ")

# l1=[3,9,2,5,6,7]
# su=0
# for i in l1:
#     su=su+i
# print(su)
# print(sum(l1))

# num=int(input("Enter a number: "))
# mul=1
# for num in range(num,1,-1):
#     print(num,end="*")
#     mul*=num
# print("1 =",mul)

# l1=[3,9,2,5,6,7]
# i=0
# while i<len(l1):
#     print(l1[i],end="")
#     i+=1
#     if i!=len(l1):
#         print(',',end=" ")

# i=int(input("Enter number between 100 and 200"))
# while i>=100 and i<=200:
#     print(i,end="_")
#     i+=1

# s1=input("Enter a statement: ")
# cc=1
# for i in s1:
#     if i==" ":
#         cc+=1
# print("The no of words is: ",cc)
#============PHALTU CODE============


# l=(3,5,7)
# for i in range(1,70):
#     if i==5:
#         continue
#     print(i,end=" ")
# print()
# for i in range(1,70):
#     if i==5:
#         break
#     print(i,end=" ")

# for i in range(1,101):
#     if(i%2==0):
#         continue
#     print(i,end="_")

# n=int(input("Number daalo: "))
# count=0
# for i in range(1,n):
#     if(n%i==0):
#         count+=1
#         if(count==3):
#             break
# if(count>=2):
#     print("it isnot prime")
# else:
#     print("it is prime")

# for i in range(1,15):
#     pass
# print("PHALTU CODE")

# for i in range(1,10):
#     if i%2!=0:
#         print(i,end=" ")
# c=0
# for i in range(1,5041):
#      c+=1
#      print(c)

# for i in range(6,1,-1):
#     for j in range(i-1,0,-1):
#         print('*',end="")
#     print()

# for i in range(1,6):
#     for k in range(5,i,-1):
#         print(' ',end="")
#     for j in range(1,i+1):
#         print('*',end="")
#     print()
# print('Cheating!')

# descri='''Hello Students!
# Welcome to string session!!'''
# print(descri)

# s1='computer'
# print(s1[4:7:2])

# num=12345
# print(num%10)



# string=input("Enter a string (for duplicate):")
# repeatset=set()
# result=""
# for char in string:
#     if char not in repeatset:
#         result+=char       
#         repeatset.add(char)  
# print(result)

# bharath
'''
char==b
check in set and add to set if not there
add letter to result if not in repeatset     // result= 'b' , set=('b')

iterate

char==h
check in set--not there--
add letter to result and repeatset          // result='bh' , set=('b','h')

char==a
check in set--not there--
add letter to result and repeatset          //result='bha', set=('b','h','a')

char==r
check in set--not there--
add letter to result and repeatset          //result='bhar', set=('b','h','a','r')

char==a                                     // REPEAT --SKIP
check in set--is there--
skip if statement

char==t
check in set--not there                     //result='bhart', set=('b','h','a','r','t')
add letter to result adn repeatset

char==h
check in set--is there                      //REPEAT--SKIP
skip if statement
'''
'''########################## FUNCTIONS ###############################'''

# def message():
#     print('hello')

# message()
# print(message())

# def sum(a,b):
#     sum=a+b
#     return sum
# print(sum(3,5))

# def message(name):
#     print('Ben',name)
# message(10)

# def message(name,period='evening'):
#     print('hello',name)
#     print('good',period)
# message(period='night',name='bharath')

# def sum(*numbers):
#     s=0
#     for n in numbers:
#         s=s+n
#     print("Sum of",numbers,'=',s)
# sum()

# def sum(a,b):
#     c=a+b
#     return c
# print('The sum of 5 and 6 =',sum(5,6))


# #MY FIRST CODE!!
# def sum(*numbers):
#     for n in numbers:
#         lis.append(n)
#         print(lis)
    
# cont='yes'
# lis=[]
# add=0
# while cont=='yes':
#     cont=input("Enter yes to add number or no to exit")
#     if cont=='yes':
#         sum(float(input()))
#     else:
#         pass
# for i in range(0,len(lis)):
#     add=add+lis[i]
# avg=add/len(lis)
# print('Sum is:',add)
# print('Average is:',avg)

# def calculator(a,b):
#     def addition(a,b):
#         return a+b
#     def subtraction(a,b):
#         return a-b
#     def multi(a,b):
#         return a*b
#     def division(a,b):
#         return( a/b)
#     print('addition',addition(a,b))
#     print('subtraction',subtraction(a,b))
#     print('product',multi(a,b))
#     print('division',division(a,b))
# calculator(40,10)

# def calculator(a,b):
#     def addition(a,b):
#         return a+b
#     def subtraction(a,b):
#         return a-b
#     def multi(a,b):
#         return a*b
#     def division(a,b):
#         return a/b
#     add,sub,mul,div=addition(a,b),subtraction(a,b),multi(a,b),division(a,b)
#     return add,sub,mul,div
# print(calculator(40,10))


'''
HW Questions:

python program to reverse order of items in array
to get number of occurences of a specified element in array
to find out if a given array of integers contains any duplicate elements
to find the missing number in the given array of 5 continuous numbers
replace all odd numbers in the given array with -1
'''
# import array as bomb
# a=bomb.array('i',[2,5,6,1,9])
# a.reverse()
# print(a)

# G1=10
# print("Global Variable within function",G2)

# def sample(n):
#     L1=0
#     global G2
#     G2=20 
#     L1=L1+n+G1+G2
#     print(L1)
# sample(10)
# print("Global Variable",G1)
# print("Global Variable within function",G2)
# #print("Local Varaible",L1)

# a=20
# def scopeDemo():
#     a=10
#     print('a=',globals()['a'])
#     print('a=',a)
# scopeDemo()

'''Recursion- is the process where function call itself from its own body,
          and that function is called as recursive function ''' 

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(3))

'''############################### MODULES ###############################'''
# from hello import gb
# gb()

# import math
# print(math.pi)
# print('exponential constant, e ',math.e)
# print('convert degree to radian',math.radians(90))
# print('math sin',math.sin(1.5707963267948966))
# print('math cos',math.cos(1.5707963267948966))
# print('math tan',math.tan(1.5707963267948966))
# print('math log',math.log(100))
# print('log base 10',math.log10(100))
# print('math powers',math.pow(3,3))
# print('math square root',math.sqrt(16))
# print('ceil',math.ceil(3.5721))
# print('floor',math.floor(3.5677))

# import random
# print(random.random())
# print(math.floor(random.random()*10))
# print(random.randint(0,9))
# print(random.randrange(0,101,10))
# print(random.choice('computer'))
# print(random.choice([12,23,34,45,56,67,78,89,100]))
# numbers=[12,23,34,45,56,67,78,89,100]
# random.shuffle(numbers)
# print(numbers)

# import random
# lucky=0
# score=0
# numluck=0 
# chance=3
# while chance>0:
#     lucky=int(input("Enter a number between 1 to 9: "))
#     numluck=random.randint(0,9)
#     print(numluck)
#     if lucky==numluck and chance==3:
#         score=10
#         break
#     elif lucky==numluck and chance==2:
#         score=7
#         break
#     elif lucky==numluck and chance==1:
#         score=5
#         break
#     chance-=1
# print("You have scored",score,'points')

'''
Write a Python program to count the number of characters in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''
# google=input("print the string ")
# de={}
# for i in google:
#     if i in de:
#         de[i]+=1
#     else:
#         de[i]=1
# print(de)

# google=input("print the string ")
# de={}
# for i in google:
#     if i in de:
#         de[i]+=1
#     else:
#         de[i]=1
'''# x=max(de,key=de.get)
# print(f"the highest frequency of {google} is '{x.upper()}' value{max(de.values())}")
'''

'''                                   LIST                             '''
# l1=[]
# print(type(l1))
# l1=list([1,2,3,4,5])
# print(l1)

# lis=[0,0,0,0,0]
# i=0
# while i<5:
#     lis[i]=input("Enter any number/value: ")
#     i+=1
# print(lis)

# l4=[101,'Ajay','ajay.s@mail.com',76567.78]
# del l4[2:4]
# print(l4)
# l4.remove(101)
# print(l4)
# l4.pop()
# print(l4)

# l1=['bharath','siva','adarsh','piyush','soham']
# print(max(l1))

# l1=[10,20,30,40]
# l1.append([50,60])
# print(l1)
# print(l1.count(30))     # here we can count the number as it is directly inside the main list
# print(l1[4].count(50))  # here we need to specify the sublist -which is at index 4 so that we can count 50.

# We cannot append two elements directly so we need to use a sublist to add 
# but the drawback is that you cant apply the methods directly to the elements of sublist. 
# to counter this, we specify the sublist when calling first then do the method, like we did in count.

# The index method in lists takes 3 arguments:
# list.index( element, start , end)
# Here the elements dont get added as sublists

# The insert method in lists takes 2 arguments:
# list.insert(index , element)
# Here elements get added as sublists if the elements are more than 1

# l1=[10,20,30,40]
# l1.extend([50,60,70,40])
# print(l1)
# print(l1.index(40,))
# l1.insert(4,80)
# print(l1)

# reverse() is a list function which reverses the list
# reversed() is a built in function which also reverses the list but you have to give list constructor outside
# l1=[10,20,40,50,60,70,80,90]
# l1.reverse()
# print(l1)
# l2=list(reversed(l1))
# print(l2)

# clear() method will clear the elements of the list i.e. will empty the list
# l1=[10,20,40,50,60,70,80,90]
# print(l1)
# l1.clear()
# print(l1)

# sort() method will sort the list in ascending order. The list should be homogenous
# default is ascending order, for descending, do reverse=True in the ( )
# to sort a list of strings, it gets sorted as per ascii codes, if want on lenth, write key=len in ( )

# l1=[14,5,7,2,34,12,55]
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)
# l2=['Adarsh','Piyush','Bharath','Soham','Siva']
# l2.sort()
# print(l2)
# l2.sort(key=len)
# print(l2)

#copy method will copy the list
# l1=[10,20,40,50,60,70,80,90]
# l2=l1.copy()
# print(l2) 

'''###################LIST COMPREHENSIONS################''' 
# just like set builder form: set={x | x belongs to N,x fulfill condition}
# like that we do here, [what to append| the loops condition | the fulfilling condition]
# eg: example= [ x for x in range(0,11) if x%2==0]

# odd_square=[]
# for x in range(0,11):
#     if x%2==1:
#         odd_square.append(x**2)
# print(odd_square)

# odd_sq=[x**2 for x in range(1,11) if x%2==1]
# print(odd_sq)


'''                                       TUPLE                              
'''
# l1=[1,2,3]
# t1=(1,2,3)
# t2=(3,4,5)
# print(t1.clear())
# print(t1.append(3))
# print(t1.reverse())
# print(t1.sort())
# print(t1.pop())
# print(t1.remove(3))
# print(l1.count(2))
#print(t1.cmp(t2))

# def palindrome(n):
#     num=str(n)
#     if num==num[::-1]:
#         return 'is palindrome'
#     else:
#         return 'isnt palindrome'
# n=int(input("Enter a number: "))
# print('Number',n,palindrome(n))
    
'''                                      DICTIONARY
'''
# d={}
# print(type(d))
# dic={'rollno':142,'name':'Piyush','age':609}
# print(dic)
# dictt=dict(rollno=142,name='Adarsh',age=12)
# print(dictt)

# student={'roll':420,'sname':'Piyush','contact':7588720672,'fees':6009.69}
# print(type(student))
# print(student)
# print(student['sname'])      # Read the sname from the dictionary
# student['contact']=9967631400    # Change the contact to the value given after []=
# print(student)
# del(student['fees'])            # Delete the 'fees' element from the dictionary
# print(student)
# student['email']='piyushsolanki1916'    # Adding the 'email' element to the dictionary
# print(student)
# student.clear()
# print(student)
# print(dir(student))

# student={'roll':420,'sname':'Piyush','contact':7588720672,'fees':6009.69}
# studd=student.copy()
# print(studd)
# print(len(student))
# print(type(str(student)))
# student.pop('contact')          # removes the term of which key is mentioned
# print(student)
# student.popitem()               # removes the last item from the dictionary
# print(student)

# student={'roll':420,'sname':'Piyush','contact':7588720672,'fees':6009.69}
# print(student.keys())
# print(student.values())
# sv=student.values()
# print(type(sv))
# print(student.items())
# print(student.get('sname'))
# dic={'email':'solankisahab@email.com'}
# student.update(dic)
# print(student)
# print(sorted(student))

'''                                     Class:-
'''
# class student:
#     def __init__(self,name):
#         self.roll=1
#         self.name=name
#         self.mark=[]
#         self.lis=[self.roll,self.name,self.mark]
#     def get_data(self):
#         print("the name is ",self.name)
#         print("roll num",self.roll)
#         print(self.lis)
#     def marks(self,ma):
#         mark=list(ma)
#         o=0
#         for i in mark:
#             o=o+i
#         print("sum=",(o))
#         print("averge is=",o//len(ma))
#     def __del__(self):
#         print('Object Destroyed')
        
        
# s=student("siva")
# s.get_data()
# t=(1,2,3,4)
# s.marks(t)
# s2=student("soham")
# s2.get_data()


# class number:
#     c=0       # class variable
#     def __init__(siva,n):
#         siva.n=n         # instance variable
#         number.c+=1
#     def display(siva):
#         print('Number',siva.n)
#     def __del__(siva):
#         print("Object Destroyed")
# obj1=number(int(input("Enter number:")))
# print(obj1.c)
# print('object 1')
# obj1.display()
# obj2=number(int(input("Enter number:")))
# print(obj2.c)
# print('object 2')
# obj2.display()


# #Python program to show variables with a value assigned in class declaration,are class variables\
# class csstudent:
#     stream='IT'             #Class Variable
#     def __init__(self,name,roll):
#         self.name=name               #instance variable
#         self.roll=roll               #instance variable

# a=csstudent('ABC',1)
# b=csstudent('DEF',2)
# print('Student 1')
# print(a.stream)
# print(a.roll)
# print(a.name)
# print('Student 2')
# print(b.stream)
# print(b.roll)
# print(b.name)

# print(csstudent.stream) 
# a.stream='ETC'
# print('a.stream',a.stream)
# print('b.stream',b.stream)
# csstudent.stream='CS'
# print('a.stream',a.stream)
# print('b.stream',b.stream)

# c=csstudent('PQR',3)
# print(c.stream)
# print(c.roll)
# print(c.name)


# class constr_types:
#     def __init__(self):
#         print('Default Constructor')
#     def __init__(self,arg1):
#         self.data=arg1
#         print('Parametrized Constructor')
# obj1=constr_types()
# obj2=constr_types(10)

# # Using the delattr in instance variable will delete the whole variable itself
# class student:
#     def __init__(self):
#         self.roll=0
#         self.sname=''
#     def setdata(self):
#         self.roll=int(input("Enter your roll no: "))
#         self.sname=input("Enter the name: ")
#     def getdata(self):
#         print('Roll No:',self.roll)
#         print('Name   :',self.sname)
# s1=student()
# s1.setdata()
# print('The name input:',getattr(s1,'sname'))
# setattr(s1,'sname','Vijay')
# print('The name after reset:',getattr(s1,'sname'))
# delattr(s1,'sname')
# print('Is name there now?:',hasattr(s1,'sname'))
# s1.getdata()


# # # Using delattr in class variable will delete only the input of variable
# class student:
#     '''this is doc string'''
#     roll=0
#     sname=''
#     def setdata(self):
#         self.roll=int(input("Enter your roll no: "))
#         self.sname=input("Enter the name: ")
#     def getdata(self):
#         print('Roll No:',self.roll)
#         print('Name   :',self.sname)
# s1=student()
# s1.setdata()
# print(getattr(s1,'sname'))
# setattr(s1,'sname','Vijay')
# print(getattr(s1,'sname'))
# delattr(s1,'sname')
# print(hasattr(s1,'sname'))
# s1.getdata()
# print(student.__dict__)
# print(student.__name__)
# print(student.__module__)
# print(student.__doc__)

# class students:
#     rollno=[]
#     namestu=[]
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def display(self):
#         students.rollno.append(self.roll)
#         students.namestu.append(self.name)
#         print("The names are:",students.rollno)
#         print("The roll no of students are:",students.namestu)
# s1=students('siva',1)
# s2=students('perni',2)
# s3=students('adarsh',3)
# s4=students('soham',4)
# s5=students('vijay',5)

''' MISTAKES   '''
      # def __init__(self,roll,*name):
    #     self.name=name
    #     self.roll=roll
    # def display(self):
    #     for i in range(max(len(self.roll,),len(self.name))):
    #         print(self.name[i],self.roll[i])

        # # students.rollno.append(self.roll)
        # # students.namestu.append(self.name)
        # print("The names are:",students.rollno)
        # print("The roll no of students are:",students.namestu)


'''                                   Python Inheritance
'''
# Syntax
# class derived_class(base class):
#      <class suite>
# Syntax ::
# class derive_class(<base class 1>,<base class 2>,....<base class n>):
#       <class suite>

# class vehicle:
#     def __init__(self):
#         self.make=''
#         self.model=''
#     def displaydetails(self):
#         print('Make:',self.make,'\nModel:',self.model)
# class swift(vehicle):
#     def __init__(self):
#         self.make='McLaren'
#         self.model='W1'
# o2=swift()
# o2.displaydetails()

# class vehicle:
#     speed=50
#     def __init__(self,mk,md):
#         self.make=mk
#         self.model=md
#     def displaydetails(self):
#         print('Make:',self.make,'\nModel:',self.model)
# class swift(vehicle):
#     speed=100
#     def __init__(self,a,b):
#         super().__init__(a,b)
#     def speed_car(self):
#         print('speed :',super().speed)
# o2=swift('Koenigsegg','Agera R')
# o2.displaydetails()
# o2.speed_car()
# print(o2.speed)

# #Hierarchical
# class student:
#     def setPersonal(self):
#         self.roll=input("Enter the roll no: ")
#         self.name=input("Enter the name: ")
#     def getPersonal(self):
#         print("Roll:",self.roll,"\nName:",self.name)

# class fy(student):
#     def getMarks(self):
#         self.s1=int(input("Enter Subject1 Marks"))
#         self.s2=int(input("Enter Subject2 Marks"))
#         self.s3=int(input("Enter Subject3 Marks"))
#     def showMarks(self):
#         self.total=self.s1+self.s2+self.s3
#         print("Total:",self.total)

# class sy(student):
#     def getMarks(self):
#         self.s1=int(input("Enter Subject1 Marks"))
#         self.s2=int(input("Enter Subject2 Marks"))
#         self.s3=int(input("Enter Subject3 Marks"))
#         self.s4=int(input("Enter Subject4 Marks"))
#     def showMarks(self):
#         self.total=self.s1+self.s2+self.s3+self.s4
#         print("Total:",self.total)
# obj1=sy()
# obj2=fy()
# #object of second year calling
# obj1.setPersonal()
# obj1.getMarks()
# obj1.getPersonal()
# obj1.showMarks()
# #object of first year calling
# obj2.setPersonal()
# obj2.getMarks()
# obj2.getPersonal()
# obj2.showMarks()

# '''For a bank customer create a base classes as savings acc and loan acc
# and create a multiple inheritance:-
# '''
# class savings:
#     def set_acno(self):
#         self.acno=input("Enter the savings acc no:")
#     def set_deposit(self):
#         self.deposit=float(input("Enter the savings acc deposit:"))
#     def get_info(self):
#         print('Account No:',self.acno,'\nAmt Deposit:',self.deposit)
    
# class loan:
#     def set_acno(self):
#         self.acno=input("Enter the loan acc no:")
#     def set_deposit(self):
#         self.deposit=float(input("Enter the loan acc deposit:"))
#     def get_info(self):
#         print('Account No:',self.acno,'\nAmt Deposit:',self.deposit)

# class maininfo(loan,savings):
#     def set_name(self):
#         self.name=input("Enter your name: ")
#     def get_name(self):
#         print('The name of account holder is:',self.name)

# info=maininfo()
# info.set_acno()
# info.set_deposit()
# info.set_name()
# info.get_info()
# info.get_name()

# class distance:
#     def __init__(self,n):
#         self.n=n
#     def __add__(self,d2):
#         result=self.n+d2.n
#         return result
#     def __sub__(self,d2):
#         result=self.n-d2.n
#         return result
#     def __lt__(self,d2):
#         result=self.n<d2.n
#         return result
# d1=distance(10)
# d2=distance(45)
# print(d1+d2)
# print(d1-d2)
# print(d1<d2)

# class myclass:
#     __hiddenVariable=0
#     def add(self,increment):
#         self.__hiddenVariable+=increment
#         print(self.__hiddenVariable)
# myobj=myclass()
# myobj.add(2)
# myobj.add(5)

'''build a class complex having attributes real and imaginary. 
and perform complex number addition and subtraction operations
'''
# class maths:
#     def __init__(self,r,i):
#         self.real=r
#         self.imag=i
#     def __add__(self,d2):
#         # result=(self.real+d2.real,(self.imag+d2.imag))
#         result=f"{self.real+d2.real} + {self.imag+d2.imag}i "
#         return result
#     def __sub__(self,d2):
#         # res=(self.real-d2.real,(self.imag-d2.imag))
#         res=f"{self.real-d2.real} + {self.imag-d2.imag}i "
#         return res
# d1=maths(2,4)
# d2=maths(3,5)
# print(d1+d2)
# print(d1-d2)

'''                                    File I/O    
'''
# file_object=open("file path","mode")
# file_object.close()

# f=open("/Users/sohamkarandikar/Documents/soham python/myfile.txt","w")
# f=open("./myfile.txt","w")
# data="ITM KHARGHAR"
# f.write(data)
# f.close()

# f=open("./myfile.txt","r")
# data = f.read()
# print("File Contents:",data)
# f.close()

# f=open("./myfile.txt","a")
# data="\nITM KHAKRA"
# f.write(data)
# f.close()

# f=open("./myfile.txt","r")
# data=f.readlines()
# print(("File Contains :",data))
# c=1
# for line in data:
#     print(c,line)
#     c+=1
# f.close()

# f=open("./myfile2.txt","w")
# data=['B.Tech CSE\n','ITM Khakra']
# f.writelines(data)
# f.close

# f=open("./myfile.txt","r")
# s=f.read(10)
# print(s)
# f.close()

# with open("./myfile.txt") as file:
#     print(file.readline())

# f=open("./myfile.txt","r")
# line=f.readline()
# while line!='':
#     print(line)
#     line=f.readline()

# with open("./myfile.txt","r") as file:
#     print(file.readlines())

# with open("./myfile.txt","r") as file:
#     for item in file:
#         print(item)

# import os
# os.mkdir('test')        # create directory
# os.chdir('test')        # change directory
# print(os.getcwd())      # give current directory path
# os.chdir("/Users/sohamkarandikar/Documents/soham python")
# os.rmdir("test")

# tell() and seek(offset,[from])
# FOR offset- We have three locations --> 0,1,2
# 0 is start, 1 is the current location and 2 is the end of file.

# with open("./myfile.txt","a") as f:
#     pos=f.tell()
#     print(pos)
  
# with open("./myfile.txt","r") as f:
#     f.seek(15,0)         # 0 as the offset value, means from start of file we count 15th byte
#     print(f.readline())

# with open("./myfile.txt","rb") as f:
#     f.seek(-15,2)          # reading in reverse from end of file, only possible in rb-binary read mode
#     print(f.readline())

# with open("./iris.csv","r") as csv:
#     first_line=csv.readline()
#     print(first_line)

# with open("./iris.csv","r") as csv:
#     all_lines=csv.readlines()
#     # print(all_lines)
#     all_lines.append("rayan timepass karta hai")
#     print(all_lines)


'''                                     Exception
'''

# 2 types of errors --> Compile time and Run time.

# x=10
# try:
#     print(x)
# except:
#     print('something went wrong')
# finally:
#     print('The "try except" is finished')

# try:
#     print(x)
# except Exception as e:
#     print("An exception occured",e)
# print("End of program")

# try:
#     print(x)
# except NameError:
#     print('something went wrong')
# finally:
#     print('The "try except" is finished')

# try:
#     print(Hello)
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")
 
# try:
#     age = int(input("Enter the age: "))
#     if age<18:
#         raise ValueError          # raise used to make error explicitly
#     else:
#         print("The age is valid")
# except ValueError:
#     print("The age is not valid")

# class MyError(Exception):
#     def __init__(self,msg):
#         self.message=msg
#     def displayError(self):
#         return self.message

# try:
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     if b==0:
#         raise MyError("Value of b cannot be zero")
#     c = a / b
# except MyError as e:
#     print("Error :",e.displayError())
# except:
#     print("Error Occured")
# else:
#     print("Division is : ",c)
# finally:
#     print("In Finally")

eheh='hello this is string'
print(eheh.split())
