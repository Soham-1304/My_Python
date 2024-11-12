# # 1. Python program to check whether the string is Symmetrical or Palindrome

# def is_palindrome():
#     return palsym.lower()==palsym.lower()[::-1]
# def is_symmetrical():
#     mid=len(palsym)//2
#     if len(palsym)%2==0:
#         pre=palsym[:mid]
#         post=palsym[mid:]
#     else:
#         pre=palsym[:mid]
#         post=palsym[mid+1:]
#     return pre==post

# palsym=input("Enter a word: ")
# if is_palindrome():
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# if is_symmetrical():
#     print("Symmetrical")
# else:
#     print("Not Symmetrical")


# # 2.Find length of a string in python without using len function

# lent=input("Enter a string (to check lenght): ")
# count=0
# for i in lent:
#     count+=1
# print(count)


# #3. Python Program to remove all duplicates from a given string

# string=input("Enter a string (for duplicate):")
# repeatset=set()
# result=""
# for char in string:
#     if char not in repeatset:
#         result+=char       
#         repeatset.add(char)  
# print(result)


# 4.Maximum frequency character in String
dhaaga=input("Enter a string: ")
lis=list(dhaaga)
print(lis)
lis.sort(reverse=False)
print(lis)
