# withour setters & getters
class Student:
    def __init__(self,age):
        self.__age = age # directly assigning values without any validation

s = Student(20) # direct access 
print(s._Student__age)    

s._Student__age = -5 # no validation
print(s._Student__age)

# with setters & getters
class Student:
    def __init__(self,age):
        self.__age = age

    # setter
    def set_age(self,age):
        if age > 0:
            self.__age = age  
        else:
            print("invalid age")
    # getter
    def get_age(self):
        return self.__age             
s = Student(15)
s.set_age(-5)
print(s.get_age())

