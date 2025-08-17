# tuples
empty_tuple = ()
print(type(empty_tuple))

# numbers
tuple_nums =(10,20,30,40,50)
print(tuple_nums)

# texts
tuple_courses = ("python","java","cloud")
print(tuple_courses)

# mixed
tuple_mixed = ("python","java","cloud",10,20,30,40,50,6.6)
print(tuple_mixed)

# empty tuple
empty_tuple = tuple()
print(type(empty_tuple))
print(empty_tuple)

# numbers
tuple_nums =tuple((10,20,30,40,50))
print(tuple_nums)

# texts
tuple_courses = tuple(("python","java","cloud"))
print(tuple_courses)

# mixed
tuple_mixed = tuple(("python","java","cloud",10,20,30,40,50,6.6))
print(tuple_mixed)

# tuple_int = tuple(10) invalid
#tuple_int = tuple((10)) invalid
tuple_int = tuple((10,))
print(tuple_int)

#list
list_nums = [10,20,30,40,50]
print(list_nums)

# list[] -> tuple() # conversion
tuple_nums = tuple(list_nums)
print(tuple_nums)

# tuple() -> list[] # conversion
list_nums = list(tuple_nums)
print(list_nums)

# Accessing data in lists
tuple_nums = (10,20,30,40,50)
first_tuple_nums = tuple_nums[0]
last_tuple_nums = tuple_nums[-1]
#indexing
print(first_tuple_nums)
print(last_tuple_nums)

#slicing
tuple_nums = [10,20,30,40,50]
print(tuple_nums[:])
print(tuple_nums[1:4:1])
print(tuple_nums[1:4:-1])
print(tuple_nums[::-1])

# print(tuple_nums[10]) # IndexError: list index out of range
# looping can be done as it's an iterable
tuple_nums = (10,20,30,40,50)
for i in tuple_nums:
    print(i)
     
# using range
tuple_nums = tuple(range(0,26,5))
print(tuple_nums)

# perform any operations with operators
tuple_nums = tuple(range(0,26,5))
for i in tuple_nums:
    print(i*2)

#perform some conditionals
days = ("sun","mon","tue","wed","thu","fri","sat")
day = input("enter day name in a week: ")
if day in days:
    print("Day exists")
else:
    print("invalid day in week")    

# Duplicates are allowed
tuple_nums = (10,20,30,40,50,50,50,30)
print(tuple_nums)

# tuple operations
tuple_nums = (10,20,30,40,50)
print(dir(tuple_nums))

# 1 index() -> returns the index position of element.
tuple_nums = (10,20,30,40,50)
print(tuple_nums.index(30))

# 2 count() -> counts and returns number of times a element present
tuple_nums = (10,20,30,40,50,10)
print(tuple_nums.count(10))

# tuples packing and unpacking
# person = ("pranay",21,"python",30000) # ValueError: too many values to unpack (expected 3)
person = ("pranay",21,"python") # packing
name,age,course = person # unpacking

print(name,age,course)

t1 = ([10,20],[30,40],[50,60])
print(t1)
t1[0][0] = 100
print(t1)

t1 = ([10,20],[30,40],[50,60])
print(t1)
t1[0][0] = 100 # valid -> changing list
print(t1)

t1 = ([10,20],[30,40],[50,60])
print(t1)
# t1[1] = [300,400] # invalid -> changing tuple # TypeError: 'tuple' object does not support item assignment  
print(t1)

l1 = [(10,20),(30,40),(50,60)]
print(l1)
# l1[0][0] = 100 # invalid # TypeError: 'tuple' object does not support item assignment  
print(l1)

print(l1)
l1[1] = (300,400)
print(l1)

