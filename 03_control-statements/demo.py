# if condition
value = 10

#check if given value is positive
if value>0:
    print(f"Given {value} is Positive")
    print("code will not execute")

# check a number is in range or not(10 to 20)
num = 13
if num>=10 and num<=20:
    print(f"Given {num} is in range")

# if-else condition
value = -10
# check if given number is positive or negative
if value>0:
    print(f"Given {value} is positive")
else:
    print(f"Given {value} is negative")  

# input() --> for taking inputs
#print("Enter Your Email: ")
email = input("Enter Your Email: ")
print(f"Welcome: {email}")

#check vote eligibility
age = int(input("Enter Your Age: "))
if age>=18:
    print(f"you can vote")
else:
    print(f"you cannot vote")  

# check vote eligibility using ternary operator
# value_if_true if condition else value_if_false
age = int(input("Enter your age: "))
status = "you can vote" if age>=18 else "you cannot vote"
print(status)

#elif condition  
avg_score = int(input("Enter your average score:"))
if avg_score>=90:
    print("A Grade")
elif avg_score>=75:
    print("B Grade")
elif avg_score>=65:
    print("C Grade")
elif avg_score>=50:
    print(("D Grade"))
elif avg_score>=35:
    print("E Grade")
else:
    print("FAIL")    

# match-case condition
choice = int(input("Enter your Choice:"))
match choice:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four") 
    case _:
        print("invalid")               

#nested conditions
#Club entry --> if age is 21 or above and also a valid ID should be present
age = 34
has_id = False
if age>=21:
    if has_id:
        print("You are allowed to enter")
    else:
        print("you need an ID to enter")
else:
    print("you are too young to enter")            
