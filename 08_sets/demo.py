# empty set
empty_set = {} # this is dict
print(type(empty_set))
print(empty_set)

# use set class
empty_set = set()
print(type(empty_set))
print(empty_set)

print(dir(empty_set))

 # numbers set
set_nums = {10,20,30,40,50}
print(set_nums) # unordered

# duplicates eliminated
set_nums = {10,20,30,40,50,10,20}
print(set_nums) # only unique elements are printed

# index will not work
set_nums = {10,20,30,40,50}
# print(set_nums[2]) # TypeError: 'set' object is not subscriptable
# unindexed

# text data
set_text = {"python","java","cloud"}
print(set_text)

# mixed data
set_mixed = {"python","java","cloud",10,20,30,40,50,5.5}
print(set_mixed)

# accessing  the data in sets
set_nums = {10,20,30,40,50}
# print(set_nums[2]) -> no indexing with sets

# print(dir(set_nums)) --> set is iterable
for i in set_nums:
    print(i)

list_nums = list(set_nums)
print(list_nums)
print(list_nums[1])

# operations/methods on sets
# add() -> add an element to set
s1 = {10,20,30,40,50}
s1.add(50)
s1.add(60)
print(s1)

#s1.add([70,80])
s1.add((70,80))
print(s1)

# update() -> adds multiple elements from iterables only
s1 = {10,20,30,40,50}
# s1.update(60) # TypeError: 'int' object is not iterable
s1.update([60,70])
print(s1)
s1.update((80,90),(10,20,30)) # accepts multiple arguments
print(s1)

# remove() -> removes a specific element, raises error if not found
s1 = {10,20,30,40,50}
s1.remove(10)
# s1.remove(60) # KeyError: 60
print(s1)

# discard() -> removes a specific element, raises no error if not found
s1 = {10,20,30,40,50}
s1.discard(60)
print(s1)
s1.discard(30)
print(s1)

# clear() -> removes all elements
s1 = {10,20,30,40,50}
s1.clear()
print(s1)

# pop() -> removes an random/arbitrary element
s1 = {10,20,30,40,50}
s1.pop()
print(s1)

# set specific operations
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# copy() -> creates a shallow copy
s1 = {10,20,30,40,50}
s2 = s1.copy()
print(s1)
print(s2)

s2.add(60)
print(s1)
print(s2)

# soft copy -> creates a soft copy using =
s1 = {10,20,30,40,50}
s2 = s1
print(s1)
print(s2)

s2.add(60)
print(s1)
print(s2)


# union() -> combines elements from both sets
print(s1.union(s2))
print(s1 | s2)

#intersection() -> extract only common elements
print(s1.intersection(s2))
print(s1 & s2)

# intersection_update() -> extract only common elements, updates the calling set
print(s1)
print(s2)
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference() -> removes the elements which also occur in the other set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1)
print(s2)
print(s1.difference(s2))
print(s1-s2)
print(s2-s1)
print(s1)
print(s2)

# difference_update() -> removes the elements which also occur in the other set and updates the calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1)
print(s2)
print(s1.difference_update(s2))
print(s1)
print(s2)

 # symmetric_difference() -> removes common elements and take combine elements left in both sets
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1)
print(s2)
print(s1.symmetric_difference(s2))
print(s1^s2)
print(s2^s1)
print(s1)
print(s2)

 # symmetric_difference_update() -> removes common elements and take combine elements left in both sets and updates calling sets
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1)
print(s2)
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset() -> checks if the given set subset of another set
s1 = {10,20,30,40,50}
s2 = {40,50} # True
#s2 = {60,40,50} #False
print(s2.issubset(s1))

# issuperset() -> checks if the given set superset of another set
s1 = {10,20,30,40,50}
s2 = {40,50} # True
print(s1.issuperset(s2))
print(s2.issuperset(s1)) # False

# isdisjoint() -> checks if two sets have no common elements
s1 = {10,20,30,40,50}
s2 = {40,50} # False
s3 = {60,70,80} # True
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# print(dir(s1))
s1 = {10,20,30,40,50} # regular set
# fs = {10,20,30,40,50} this is also set

#frozenset canbe created  using class frozenset
fs = frozenset({10,20,30,40,50})
print(type(fs))
print(fs)
# print(fs.add(60)) # AttributeError: 'frozenset' object has no attribute 'add'   
print(dir(fs))

# frozenset operations 
fs1 = frozenset({10,20,30,40,50})
fs2 = frozenset({40,50,60,70,80})

print(fs1.union(fs2))






