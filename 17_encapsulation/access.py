# private
class A:
    def __init__(self,a,b):
        self.__a = a  # private
        self.__b = b  # private

obj = A(10,20)

# accessing private
print(obj._A__a) # name mangling
print(obj.b)
