#print(hello)
#print(9)
#print("a")
#a=10
#b=20
#print(a+b)
#import keyword
#print(keyword.kwlist)
#from math import sqrt
#print(sqrt(16))
student_name_1 = "pranay"
print(type(student_name_1))
print(id(student_name_1))
student_name_2 = "ghanta"
print(id(student_name_2))
student_age_1 = 22
print(type(student_age_1))
print(id(student_age_1))
student_age_2 = 22
print(id(student_age_2))
student_gpa = 7.0
print(type(student_gpa))
print(id(student_gpa))
list_1 = [1,2,3]
list_2 = [1,2,3]
print(id(list_1))
print(id(list_2))
x = "python"
y = " is"
z = " awesome"
print(x+y+z)
x = 10
y = 20
print(x+y)
z = " awesome"
#print(x+z) -->TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(x,z)
x,y,z = "one","two","three"
print(x,y,z)
#x,y,z = "one","two","three","four"
#    x,y,z = "one","two","three","four"-->ValueError: too many values to unpack (expected 3)

print(x,y,z)
x=y=z="one"
print(x)
print(y)
print(z)