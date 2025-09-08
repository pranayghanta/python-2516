# duck typing

class Duck:
    def quack(self):
        print("duck sounding")

class Person:
    def quack(self):
        print("i can also quack like duck")    

def make_quack(obj):
    obj.quack()
make_quack(Duck())            
make_quack(Person())            
