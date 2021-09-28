
# new_str = input('Enter any string: ')
name = "ABCDEFGHIJKLMNOPQRST"

#print(str(name[3])+" "+str(new_str))

# name[2] = "x" -->  Can't do this thing

print(name[2:6]) # string slicing
print(name[:5]) # 0th to (5-1)th index
print(name[5:]) # (5)th to (n-1)th index
print(name[4:-5]) # it will slice the string from back side


print(name[:0:-1]) # it will print the string reverse
 

 
print(name[0::3]) # it skipes two values 
print(name[0::2]) # it skipes one values 
print(name[4:15:2]) #it skipes one values  in given range


 
