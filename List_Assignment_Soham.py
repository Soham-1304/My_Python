# 1.Write a Python program to remove duplicates from a list.
def dupp(lis):
    lis=list(set(lis))
    print(lis)
dupp([1,4,3,5,2,4,1,5,3,1,4])


# 2.Write a Python function that takes two lists and returns True if they have at least one common member
def lists(lis1,lis2):
    for i in lis1:
        if i in lis2:
            return True
    return False
print(lists([1,2,3,4,5],[9,8,7,6,5]))


# 3.Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove_even(olist):
    olist=[i for i in olist if i%2!=0]
    print(olist)
remove_even([12,23,34,45,56,67,78,89,100])


# 4.Write a Python program to find the second smallest number in a list.
def smallnum2(numlist):
    numlist.sort(reverse=False)
    print("The second smallest number in the list is:",numlist[1])
smallnum2([12,34,66,23,73,17,84,62,52,92])


# 5.Write a Python program to split a list every Nth element.
def splitlist(splitl,count):
    splitl=[splitl[i:i+count] for i in range(0,len(splitl),count)]
    return splitl
count=int(input("Enter the N th element for dividing the list: "))
print(splitlist([1,2,3,4,5,6,7,8,9,10],count))


# 6.Write a Python a function to find the union and intersection of two lists.
#Method1:
def union_intersection(lst1,lst2):
    union=list(set(lst1)|set(lst2))
    intersection=list(set(lst1)&set(lst2))
    return union,intersection
lst1=[1,2,3,4,5,6,7,8,9,10]
lst2=[16,15,14,13,12,11,10,9,8,7]
union,intersection=union_intersection(lst1,lst2)
print('Union is:',union)
print('Intersection is:',intersection)

#Method2:
def un_inter(l1,l2):
    un=list(set([x for x in l1 +l2]))
    inter=[x for x in l1 if x in l2]
    return un,inter
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[16,15,14,13,12,11,10,9,8,7]
un,inter=un_inter(l1,l2)
print('Union is:',un)
print('Intersection is:',inter)


# 7.Write a Python function to check if a list is a palindrome or not. Return true otherwise false
def is_palindrome(leest):
    if leest[::-1]==leest:
        return True
    else:
        return False
print(is_palindrome([1,2,3,4,5,4,3,2,1]))
