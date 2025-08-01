#strings
#single line strings
data_1 = "hello"
data_2 = 'hello'
data_3 = '''hello'''
data_4 = """hello"""
print(data_1)
print(data_2)
print(data_3)
print(data_4)

#multi line strings
#python_desc = "Python is a computer programming language often used to build websites and software, automate tasks, and analyse data. Python is a general-purpose language, not specialised for any specific problems, and used to create various programmes"
python_desc = """Python is a computer programming language often used to build websites and software, automate tasks, and analyse data. Python is a general-purpose language, not specialised for any specific problems, and used to create various programmes"""
 
question = "How are you?"
#using a single quote inside single is not valid
#if you want to include single quote,use  double quotes
#answer = 'i'm fine'
answer = "i'm fine"
print(answer)

#answer = "im "good""
answer = 'im "good"'
print(answer)

# if we want both use ''' or """
answer = """i'm fine and "good" """
print(answer)

#accessing
text = "python"

# it uses indexing to access individual characters
print(text[0])
print(text[2])

print(text[-2])

#invalid range
#print(text[10])#IndexError: string index out of range

text = "python"
#using for loop to access each individual character
for i in text:
    print(i)

#slicing
text = "python"
print(text[0:3])# last is excluded -> pyt
print(text[1:4])# last is excluded -> yth
print(text[1:])# last is excluded -> ython
print(text[:4])# last is excluded -> pyth
print(text[:])# last is excluded -> python

#if step is not defined,by default step is 1
print(text[1:4:1])#last is excluded -> yth
text = "pythonisveryeasytolearn"
text1 = "python is very easy to learn"
print(text[0:16:2])# last is excluded -> pt
print(text1[0:16:2])# last is excluded -> pt
    
# for negative indexing
text = "python" 
#print(text[1:4:0])#ValueError: slice step cannot be zero
print(text[-4:-1])#tho
print(text[-4:-1:1])#tho
print(text[-4:-1:-1])# we get nothing ,because its invalid

#use case of backward step
text = "python"
print(text[::-1])

#ohty
print(text[-2:-5:1])
print(text[-2]+text[-3]+text[-4]+text[-5])

text = "Python"
print(text[4:0:-1])
print(text[-2:-6:-1])


#string immutability
text = "python"
#text[0] "P"
print(text) 

#reassigning
text = "python"
text = "Python"
print(text)

new_text = "J" + text[1:]
print(new_text)

#Concat & repeat
#concat can join multiple strings
str = "hi"
print(str * 5)

#String operations -> string methods
print(dir(str))

mobile_number = input("Enter Mobile Number: ")
valid_number = mobile_number.isdigit()
print(valid_number)

pan_number = input("Enter Pan Number: ")
valid_pan_number = pan_number.isalnum()
format_valid_pan_number = pan_number.upper()
print(format_valid_pan_number)

#every method functionality
print(help(str.isupper))
