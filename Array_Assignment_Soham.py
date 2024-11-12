# 1.Write a Python program to reverse the order of the items in the array.
import array as rev
a=rev.array('i',[2,5,6,1,9])
print(a)
a.reverse()
print(a)


# 2.Write a Python program to get the number of occurrences of a specified element in an array.
import array as occur
arr=occur.array('i',[2,5,7,2,6,3,1,9,7,3,5,4,1,8,1])
spec=int(input("Enter the number to count its occurence: "))
count=0
for i in arr:
    if i==spec:
        count+=1
print('The number',spec,'has occured',count,'times in the array')


# 3.Write a Python program to find out if a given array of integers contains any duplicate elements.
import array as dupe
arr=dupe.array('i',[2,5,7,2,6,3,1,9,7,3,5,4,1,8,1])
set_arr=set(arr)
duplicates=len(arr)-len(set_arr)
print("The array has",duplicates,'duplicate integers')


# 4.Write a  Python program to find the missing number in a given array of 5 continuous numbers.
import array as missing
arrey=missing.array('i',[3,4,6,7])
misnum=0
for i in range(0,len(arrey)-1):
    if arrey[i+1]-arrey[i]==2:
        misnum=arrey[i]+1
print("The missing number from the array is",misnum)


# 5.Replace all odd numbers in the given array with -1
import array as replace
odd=replace.array('i',[1,2,3,4,5,6,7,8,9,10])
for i in range(0,len(odd)):
    if odd[i]%2!=0:
        odd[i]=-1
print(odd)
