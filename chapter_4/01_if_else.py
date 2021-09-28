a = 45

if(a > 3):
    print("The value is greater than 3")
elif (a > 7):
    print("The value is less than 40")
else:
    print("The number is 45")

if a > 3:
    print("Greater than 3")
if a > 15:
    print("Greater than 15")
if a > 40:
    print("Greater than 40")



b = [44, 30 ,25]
if 44 in b:
    print("YES")
else: 
    print("No")


P = 10
Q = 15

# use of 'and'
if (P < 12 and Q < 12): 
    print("YES")
else: 
    print("NO")

# Use of 'or'

if (P < 12 or Q < 12): 
    print("YES")
else: 
    print("NO")


text = "Money is everything in life"

if("every" in text): 
    print("YES present")
else:
    print("Not present")


names = ["Abhi", "Durjoy", "Sahil", "Rakesh"]
spam = "Abhi"

if(spam in names):
    print("Yes present Names")
else : 
    print("Not present names")