# exception handling
# when there are no errors, nothing to handle 
print("program execution started")
num1 = 10
num2 = 5
print(num1/num2)
print("program execution completed")
print("="*50)

# when there are errors, see how python handles them 
print("program execution started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero # division by zero is undefined in mathemetics
print("program execution completed")
print("="*50) 

# when there are errors, see how you can handle the errors - single error
print("program execution started")
num1 = 10
num2 = 5
# ZeroDivisionError: division by zero
try:
    print(num1/num2) 
except:
    print("oops! you cannot divide by zero in maths it's undefined")
print("program execution completed")
print("="*50) 

# when there are errors, see how you can handle the errors - multiple errors
import sys
print("program execution started")
data = [1,2,'python',0,5]
data = [1,2,3,4,5]
for i in data:
    try:
        print(1/i)
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero  ---> 0
    except TypeError:
        # print(sys.exc_info())
        print("oops! don't pass strings, we cannot divide strings and numbers")
    except ZeroDivisionError:
        print("oops! you cannot divide by zero in maths it's undefined") 
print("program execution completed")
print("="*50)

# when there are errors, see how you can handle the errors - single error
print("program execution started")
num1 = 10
num2 = 5
# ZeroDivisionError: division by zero
try:
    print(num1/num2) # login info is correct
except:
    print("oops! you cannot divide by zero in maths it's undefined")
else:
    print("calculation successful") # otp verify --> only when the login info is correct
finally:
    print("program execution completed")
print("="*50) 

# exception class
# print(help(Exception))
# based on my req --> we need a custom exception

class InvalidScoreError(Exception):
    pass

try:
    score = int(input("enter score (0-100): "))
    if score < 0 or score > 100:
        raise InvalidScoreError("score must be between (0-100)")
    print("your score is valid")
except InvalidScoreError as e:
    print("Error: ",e)  

class AgeTooYoungError(Exception):
    pass
class NoIDError(Exception):
    pass   
try:
    age = int(input("enter your age: "))    
    if age < 18:
        raise AgeTooYoungError
    has_id = input("Do you have id ? (yes/no)")
    if has_id != "yes":
        raise NoIDError
except AgeTooYoungError:
    print("you must be at least 18 years old to register")
except NoIDError:
    print("you must have an ID to register")
else:
    print("registration successful")





