# Method Resolution Order
class A:
    def show(self):
        print("A SHOW")

class B():
    def show(self):
        print("B show")

class C(A,B):
    pass        

obj = C()
obj.show()
print(C.mro())

# super()
class Parent:
    def greet(self):
        print("Hello from parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from child")

child = Child()
child.greet()        

