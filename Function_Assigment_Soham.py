'''1.Write a Python function to check whether a number falls within a given range.'''

def inrange(num):
    if num in range(0,101):
        print("The number is between the defined range of 1 and 100!")
    else:
        print("The number is NOT between the defined range of 1 and 100!")
inrange(int(input("Enter a number: ")))


''' 2.Write a Python function that takes a list of strings as input and 
    returns a tuple containing the shortest and longest word from the lis'''

def quest():
    strings=input("Enter the strings separated by space: ")
    lis=strings.split()
    maxi=max(lis,key=len)
    mini=min(lis,key=len)
    lis2=[]
    lis2.append(mini)
    lis2.append(maxi)
    print(tuple(lis2))
quest()


''' 3.Write a Python function that takes a list and an element as input. 
    The function should add the element to the list only if it's not already present in the list.'''

def quest3():
    l1=[]
    i=1
    while i>0:
        ele=input("Enter an element to verify in list and type 'exit to end: ")
        if ele not in l1 and ele!='exit':
            l1.append(ele)
            print("element added successfully!")
        elif ele in l1 and ele!='exit':
            print(f'{ele} is already in the list!')
        elif ele=='exit':
            break
        i+=1
    print(l1)
quest3()


'''4.Write a program to implement these formulae of permutations and combinations. 
     Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.
     Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r! '''

def pnc(n,r,type):
    def factorial(x):
        if x==0:
            return 1
        else:
            return x*factorial(x-1)
    if type=='p':
        return factorial(n)//factorial(n-r)
    elif type=='c':
        return factorial(n)//(factorial(r)* factorial(n-r))
    else:
        raise ValueError("Invalid Type input, enter p for permutation and c for combination!")
while True:
    n=int(input("Enter the 'n' objects: "))
    r=int(input("Enter the 'r' objects taken: "))
    type=input("Enter p for permutation and c for combination: ")
    if type not in ['p','c']:
        print("Invalid input,enter p for permutation and c for combination!")
    elif r>n:
        print("r cannot be greater than n !")
    else:
        result=pnc(n,r,type)
        print('Result is: ',result)
        break


'''5.A number is called perfect if the sum of proper divisors of that number is equal to the number.
    For example 28 is perfect number, since 1+2+4+7+14=28. 
    Write a program to print all the perfect numbers in a given range'''

def perfect():
    perf=[]
    for i in range(1,1000):
        l1=[]
        for j in range(1,(i//2)+1):
            if i%j==0 and i!=j:
                l1.append(j)
        if sum(l1)==i:
            print(f"{i} is a perfect number")
            perf.append(i)
        l1.clear()
    print(perf)
perfect()


'''6.Write a recursive function that will return the nth term of the Fibonacci sequence.
    The sequence has a relationship of Fn = Fn-1 + Fn-2 with F0 = 0 and F1 = 1, where n=0,1,2,3,4,5,...
    Note: I have started fibonacci series from 1, google is showing both 0 and 1.'''

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fib=int(input("Enter the 'n'th term of fibonacci you need: "))
print(f"The {fib} th term of fibonacci is :",fibonacci(fib))
        

