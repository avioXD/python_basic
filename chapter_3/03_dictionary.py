'''
In dictionary we can save value with key
by the key we can access the dictionary

> We declear dictionary like {"key": ["value1", value2]}
> Dictionary is mutable
'''


myDict = {
    "Fast": ["In a quick way ", "As soon as "],
    "Abhishek": "A Student",
    "marks": [40, 65, 72 ,80],
    "Anathor Dictionary": {
        "Dict1": "Example 1",
        "Dict2": "Example 2",
        "Dict3": [1,2,3]
    }
}   


print(myDict)
print(myDict['Fast'])
print(myDict["marks"][2])
print(myDict["Anathor Dictionary"]["Dict3"][1]) 

## Mutation of Dictionary 

myDict["Abhishek"] = "A programer"
print(myDict["Abhishek"])
myDict["Anathor Dictionary"]['Dict2'] = "Mutated"
print(myDict)


# functions

print(list(myDict.keys())) # return all the keys 
print(myDict.values()) # return all the values ins the dict
print(myDict.items()) #it will return keys as well as values

updateDict = {
    "marks": [82,70,63,85]
}

myDict.update(updateDict) #update any pair
print(myDict)


'''
    difference between dict.get() and dict['key']: 
    ...............................................
    >> Both cases it returns the value of the present key but 
    if we put any wrong key then in case of .get() method it shows 
    none or doesn't return any value but in case of dict['key']
    it throws an error so we have to be responsible for it
    
    example : 
    print(myDict.get("marks"))
    print(myDict['marks'])
    >> return  
    [82, 70, 63, 85]
    [82, 70, 63, 85]

    print(myDict.get("mark"))
    print(myDict['mark'])
    >> return 
    None
    print(myDict['mark'])
    KeyError: 'mark'
'''
print(myDict.get("marks"))
print(myDict['marks'])



