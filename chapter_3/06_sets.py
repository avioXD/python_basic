'''
>> we declear sets by using '{}' parenthesis 
>> Set is mutable
>> Set is a collection of non repetative elements
'''


a = {1 ,2 ,3 , 5} # Wrong approch
print(type(a)) #<class 'set'>
print(a)

'''
## If we put any repetative element in set then it will only reflect the one of the all
'''
b = {1 , 2 , 1, 3 , 1 , 3 , 4 }
print(b)  # {1, 2, 3, 4}

'''
## if we tried to create a empty set its not possible 
because it will detect as a dictionary
so to over come it we have to follow this syntax
'''
s= {} # Wrong approch
print(type(s)) # <class 'dict'>

s = set()
s.add(4)
s.add(8)
s.add(3)
s.add(2)
s.add(1) # add items
print(s) #{1, 2, 3, 4, 8}
print(len(s))
s.discard(3) # remove item
print(s) # {1, 2, 4, 8}
print(len(s))



'''
## We can't put hashable items into dictionary
if we do this : 

s.add((10 ,12 ,13))
s.add({4:5})  
print(s)

it will throw error like this : 

Traceback (most recent call last):
  File "e:\Python\Basics\chapter_3\06_sets.py", line 32, in <module>
    s.add({4:5}) # We can't put hashable items into dictionary
TypeError: unhashable type: 'dict'
'''
 

# some of union intersection difference and grouping in sets

engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice']) 
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers   # union
engineering_management = engineers & managers     # intersection
fulltime_management = managers - engineers - programmers  # difference
print(engineers , programmers, managers)
print(employees)
print(engineering_management)
print(fulltime_management)
for group in [engineers, programmers, managers, employees]: 
     group.discard('Susan')          # unconditionally remove element
     print(group)

'''
{'John', 'Jack', 'Jane', 'Janice'} {'Jack', 'Sam', 'Janice', 'Susan'} {'Jack', 'Susan', 'Zack', 'Jane'}
{'John', 'Zack', 'Susan', 'Jane', 'Janice', 'Jack', 'Sam'}
{'Jack', 'Jane'}
{'Zack'}
{'John', 'Jack', 'Jane', 'Janice'}
{'Jack', 'Sam', 'Janice'}
{'Jack', 'Zack', 'Jane'}
{'John', 'Zack', 'Jane', 'Janice', 'Jack', 'Sam'}
'''


# important topic

s = set([20, "20", 20.0])
print(s) # {'20', 20}
print(len(s)) # 2 