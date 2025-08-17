# dictionaries
empty_dict = {}
print(type(empty_dict))
print(empty_dict)

# dictionaries -> {key:value}

# numbers dict
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
# print(dict_nums[0]) # KeyError: 0
print(dict_nums[3]) 

# text dict
dict_text = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_text)
print(dict_text["course1"])

# mixed dict
dict_mixed = {1:10,"course1":"python"}
print(dict_mixed)
print(dict_mixed["course1"])

# dict inside dict
students = {10:{"name":"pranay","age":21},11:{"name":"ghanta","age":21}}
print(students)

# incorrect
# nums ={[1,2,3]:"python"} # TypeError: unhashable type: 'list'
nums ={(1,2,3):"python"}
print(nums)

# this is possible
dict_sub_dict = {10:["pranay",21],11:("ghanta",21)}
print(dict_sub_dict)

# update data ---> methods
fruits = {"a":"apple","b":"banana"}
print(fruits)
# use assignment 
fruits["c"] = "cherry"
print(fruits)

#  use assignment to update existing item
fruits["a"] = "apricat"
print(fruits)

# class dict same as lists and tuples
empty_dict = dict()
print(type(empty_dict))
print(empty_dict)

# dictionaries -> {key:value}

# numbers dict
dict_nums = dict({1:10,2:20,3:30})
print(dict_nums)
print(dict_nums[3]) 

#dict operations
print(dir(dict_nums))

# 1 update() -> adds/updates the dict items
fruits = {"a":"apple","b":"banana"}
print(fruits)
fruits.update({"c":"cherry"})
print(fruits)

# pop() -> removes items with specified keys
fruits = {"a":"apple","b":"banana"}
print(fruits)
# fruits.pop("c") # KeyError: 'c'
fruits.pop("b")
print(fruits)
# fruits.pop() # TypeError: pop expected at least 1 argument, got 0
print(fruits)

#popitem() -> removes the last inserted item
fruits = {"a":"apple","b":"banana"}
print(fruits)
fruits.update({"c":"cherry"})
print(fruits)
fruits.popitem()
print(fruits)

# fruits.popitem("b") # TypeError: dict.popitem() takes no arguments (1 given)      
# clear() -> removes all items
fruits = {"a":"apple","b":"banana"}
print(fruits)
fruits.clear()
print(fruits)

#access related methods

# get() -> get the value for key
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
print(dict_nums[3]) 


print(dict_nums.get(0)) # no key no error

#keys() -> returns all the keys only
dict_nums = {1:10,2:20,3:30}
print(dict_nums.keys())

dict_nums = {1:10,2:20,3:30}
only_keys = dict_nums.keys()
for i in only_keys:
    print(i)

#values() -> returns all the values
dict_nums = {1:10,2:20,3:30}
print(dict_nums.values())

dict_nums = {1:10,2:20,3:30}
only_values = dict_nums.values()
for i in only_values:
    print(i)

# items() -> returns both keys and values
dict_nums = {1:10,2:20,3:30}
print(dict_nums.items())

# copy() -> creates a shallow copy
dict_nums = {1:10,2:20,3:30}
bk_dict_nums = dict_nums.copy()
print(dict_nums)
print(bk_dict_nums)

bk_dict_nums.update({4:400})
print(dict_nums)
print(bk_dict_nums)

# soft copy using assignment
dict_nums = {1:10,2:20,3:30}
bk_dict_nums = dict_nums
bk_dict_nums.update({4:400})
print(dict_nums)
print(bk_dict_nums)

# setdefault() -> returns value of a key,if not present sets it
# if the key is present, will not update
dict_nums = {1:10,2:20,3:30}
print(dict_nums)

dict_nums.setdefault(4,400)
print(dict_nums)

dict_nums = {1:10,2:20,3:30,1:100,4:100}
print(dict_nums)


