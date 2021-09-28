story = "Once upon a time there was a boy called Abhishek he became the senior developer of microsoft"


print(len(story))
print(story.endswith("microsoft"))
print(story.count("a"))# count of any alphabet 
print(story.count("boy"))# give the cound of any word
print(story.capitalize()) #capitalize

print(story.find("Abhishek")) #word index of its position
print(story.replace("Abhishek", "Avio")) #replace the word

#replace example
letter = '''Dear <|name|> ,
you are selected for our company 
Date : <|Date|>
'''
name = input('Enter name: ')
date =  input('Enter date: ')

letter = letter.replace("<|name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)

#use of '\n' '\t'
story = "Once upon a time\n there was\t a boy called Abhishek\he became  the senior developer of \\ microsoft"
print(story)


#find function 
story = "Once upon a time there  called   Abhishek he became the   senior developer of microsoft"

doublespace = story.find("  ")
print(doublespace)
story = story.replace("   "," ")
story = story.replace("  "," ")
print(story)
 
 