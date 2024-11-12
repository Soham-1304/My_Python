# 1.Write a Python program to remove an item from a set if it is present in the set.
def in_set(seet,item):
    for i in range(0,len(seet)):
        if item in seet:
            seet.remove(item)
    print(seet)
in_set({'soham','bharath','siva','adarsh'},'soham')


# 2.Write a Python program to check if two given sets have no elements in common.
def check_set(s1,s2):
    count=0
    for i in s1:
        if i in s2:
            count+=1
    if count==0:
        print('The sets have no common elements')
    else:
        print(f"The sets have {count} common elements")
check_set({12,23,34,45,56,67,78,89,100},{8,16,24,32,40,48,64,72,80})


# 3.Write a Python program toGet Only unique items from two sets
def uniq_set(set1,set2):
    set3=set([x for x in set1 if x not in set2]+[x for x in set2 if x not in set1])
    return set3
unique=uniq_set({1,2,3,4,5,6},{4,5,6,7,8,9})
print(unique)


# 4.Write a Python program to Convert Set to one String
def convert_set(seat):
    chain=''
    for i in seat:
        chain=chain+str(i)
    print(chain)
convert_set({1,2,3,4,5,6,7})


# 5.Program to count number of vowels using sets in given string
def is_vowel(stirng):
    count=0
    vowel=set({'a','e','i','o','u','A','E','I','O','U'})
    for i in stirng:
        if i in vowel:
            count+=1
    print('The number of vowels in the string is:',count)
is_vowel('soham is very obedient')
