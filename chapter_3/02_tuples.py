'''
The main difference between List and Touple is
* > Can't update Touple values but can update list Value

1. Touple object doesn't support item assignment
2. Touple is a immutable data type in python
3. To make Touple we use '()' parenthesis
'''

t = (1,2,3,4,5)

empty_t = ()
# (X) t1 = (1)  # wrong way to declear a touple with single element
t1 = (1, ) #right way to declear a touple with single element

print(t)
print(t1)

t2 = (1 ,2, 1 ,3 ,  5 , 1 ,4,2 )
print(t2.count(1)) # number of occurance of the touple element 
print(t2.index(4)) # return the index number of the value