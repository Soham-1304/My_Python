# roll=101
# sname='amit'
# contact=34435453345
# print("Roll No: ",roll,"\nName",sname,"\nContact No:",contact)

# print(~12)
# # 0101
# # 1010
# print(bin(-5))

# a=5
# b=~5
# food='ice cream'
# print('My favourite food is',food,sep=':D\n')

# print('Hello'); print('World')
# print('Python',end=' '); print('Is Trash')

# print('Result of Experiment ',10 ,sep='is',end="!")

def is_palindrome():
    return palsym.lower()==palsym.lower()[::-1]
def is_symmetrical():
    mid=len(palsym)//2
    if len(palsym)%2==0:
        pre=palsym[:mid]
        post=palsym[mid:]
    else:
        pre=palsym[:mid]
        post=palsym[mid+1:]
    return pre==post

palsym=input("Enter a word: ")
if is_palindrome():
    print("Palindrome")
else:
    print("Not Palindrome")
if is_symmetrical():
    print("Symmetrical")
else:
    print("Not Symmetrical")
