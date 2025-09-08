# polymorphism
class Dog:
    def speak(self):
        print("Dog woof")
    
class Cat:
    def speak(self):
        print("Cat meow") 
dog = Dog()
cat = Cat()   

dog.speak()
cat.speak()

# predefined --> use cases for polymorphism
print(len("Python"))
print(len([1,2,3]))
print(len({"A":1,"B":2}))

# based on operators (operators overloading)
print(2 + 3)
print("hi" + " how are you")
print([1,2] + [3])

# common use case functionality
class circle:
    def area(self):
        return 3.14*5*5

class square:
    def area(self):
        return 5*5

def print_area(shape):
    print("Area", shape.area())

print(print_area(circle()))
print(print_area(square()))   

# real world use case --> database connection
class MySQL:
    def connect(self):
        return "connected to mysql"
class PostgreSQL:
    def connect(self):
        return "connected to postgresql"
def open_db_connection(db):
    print(db.connect())
open_db_connection(MySQL())
open_db_connection(PostgreSQL())    

# method overloading - not accepted in python
class mathops:
    def add(self,a,b):
        return a + b
    def add(self,a,b,c):
        return a + b + c
add_obj = mathops()
print(add_obj.add(2,3))   # TypeError: mathops.add() missing 1 required positional argument: 'c'
print(add_obj.add(2.4,3.6,7.7))   

# Duck typing in python



            