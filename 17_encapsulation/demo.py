# encapsulation

# public
class A:
    def __init__(self,a,b):
        self.a = a  # public
        self.b = b  # public

obj = A(10,20)

# accessing
print(obj.a)
print(obj.b)

# protected
class A:
    def __init__(self,a,b):
        self._a = a  # private
        self._b = b  # private

obj = A(10,20)

# accessing protected
print(obj.a)
print(obj.b)


# private
class A:
    def __init__(self,a,b):
        self.__a = a  # private
        self.__b = b  # private

obj = A(10,20)

# accessing private
print(obj.a)
print(obj.b)



