# overriding

class Animal:
    def sound(self):
        print("Animal making sound")

class Dog(Animal):
    def sound(self):
        print("Dog making sound")

class Cat(Animal):
    def sound(self):
        print("Cat making sound")

a = Animal()
a.sound()                        
d = Dog()
d.sound()
c = Cat()
c.sound()