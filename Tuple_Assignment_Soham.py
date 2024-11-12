# 1.Write a Python program to compute the element-wise sum of given tuples.             
#   Original :    (1, 2, 3, 4)   (3, 5, 2, 1)   (2, 2, 3, 1)
#   Element-wise sum of the said tuples:  (6, 9, 8, 6)
def sumtuple(t1,t2,t3):
    sumtup=[]
    temp=0
    for i in range(0,len(max(t1,t2,t3))):
        temp=t1[i]+t2[i]+t3[i]
        sumtup.append(temp)
    sumtup=tuple(sumtup)
    return sumtup
call=sumtuple((1,2,3,4),(3,5,2,1),(2,2,3,1))
print(call)


#  2.Write a Python program to convert a given list of tuples to a list of lists. 
#    Original list of tuples: [(1, 2), (2, 3), (3, 4)]
def lol(l1):
    for i in range(0,len(l1)):
        l1[i]=list(l1[i])
    print(l1)
lol([(1,2),(2,3),(3,4)])


# 3.Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
# PS: I think question is wrong, it might be convert list of list into list of tuples
#     To make the list of tuple into list of list, refer to Q2 above.
def convert(lis):
    for i in range(0,len(lis)):
        lis[i]=tuple(lis[i])
    print(lis)
convert([[1,2],[2,3],[3,4]])


# 4.Write a Python program to remove an empty tuple(s) from a list of tuples.
def remove_empty(lis1):
    lis1=[lis1[i] for i in range(0,len(lis1)) if lis1[i]!=()]
    print(lis1)
remove_empty([(100,200),(),(200,300),(),(300,400)])


# 5.Write a Python program to convert a given string to a tuple
def convert_string(stri):
    stri=tuple(stri)
    print(stri)
    print(type(stri))
convert_string('hello')


# 6.Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
def tuple_product(tup):
    prod=1
    for i in range(0,len(tup)):
        prod=tup[i]*prod
    print(prod)
tuple_product((6,4,8,2,7,9))