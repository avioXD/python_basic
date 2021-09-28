def greet(name):
    print("Good morning", name)

greet("Akshay")

''''
Functions are two types in python
1. Built in function
2. User define function
'''

#factorial of a numebr

def fact(n):
    product = 1
    for i in range(1,n+1):
        product*=i
    return product

print(fact(5))


# use of recursion

def factRec(n):
    if n == 1:
        return 1
    else:
        return n*factRec(n-1)

print(factRec(80))