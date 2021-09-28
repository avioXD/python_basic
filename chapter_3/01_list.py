
'''
The main difference between List and Touple is
* > Can't update Touple values but can update list Value

1. List  object does support item assignment
2. List is a mmutable data type in python
3. To make Touple we use '[]' parenthesis
'''


a = [6,7,8,9,20,1,2,3,4,5]
print(a)
a.sort()
print(a)

c = [45, "Abhishek Das", False, 53.8 ]
print(c)

friends = ["Tanmoy", "Sarthak","sampad","samrat","Arindam","Shila"]
print(friends)
print(friends[0:4])
print(friends[:-4])
friends.sort() # it sort the list alpgabatical order
print(friends)
friends.reverse() # it reverse the list
print(friends)
friends.append("Anirban") # it append element end of the list
print(friends)
friends.insert(2,"Ritwik") # it insert element at the given index 
print(friends)
friends.remove("Ritwik")# it remove the element
print(friends)
friends.pop(4) #it removes element by the index
print(friends)


