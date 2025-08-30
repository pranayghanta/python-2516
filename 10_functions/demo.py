# without functions
a = 10
b = 20 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 14
b = 16 

print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 200
b = 300
# define a function
def arithmetic():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# call a function
arithmetic()

a = 1000
b = 2000
# call a function -> 1000,2000
arithmetic()

# functions with parameters
def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# call a function -> 1000,2000
# arithmetic() #TypeError: arithmetic() missing 2 required positional arguments: 'a' and 'b'
arithmetic(5000,1000)
arithmetic(100,300)
# arithmetic(233) # TypeError: arithmetic() missing 1 required positional argument: 'b'

# positional arguments
def login(username,password):
    if username == "pranay" and password == "3333":
        print("login success")
    else:
        print("login failed")

login("pranay","3333")# exact order            
login("pranay","333")# exact order            
login("3333","pranay")# order changed           

# default arguments
def emp_info(emp_name,emp_email,emp_loc="hyderabad",address="india"):
    print(f"hi {emp_name} your email is {emp_email} and location is {emp_loc} actually from {address}")
#emp_info("pranay","pranay@gmail.com","hyderabad")    
emp_info("ghanta","ghanta@gmail.com")    
emp_info("user","user@gmail.com")
emp_info("ram","ram@ gmail.com","lucknow","USA")

# keyword arguments
def emp_info(emp_name,emp_email,emp_loc,address="india"):
    print(f"hi {emp_name} your email is {emp_email} and location is {emp_loc} actually from {address}")
emp_info(emp_name="ram",emp_loc="lucknow",emp_email="ram@ gmail.com")

# arbitrary positional arguments
def add_all(*numbers):
    total = 0 
    for i in numbers:
        total = total + i
    print(f"total is: {total}")    

add_all(1)
add_all(1,2)
add_all(1,2,3,4,5,6,7,8,9)

# arbitrary keyword arguments
def profile(**info):
    print(info)

profile()    
profile(id = "101")    
profile(id = "102",name = "pranay")    
profile(id = "102",name = "pranay",rating = 4.5)    

# transactions
def cred_trans(**trans):
    print(trans)
    total = 0
    for i in trans:
        total = total + trans[i]
    print(f"you have done {len(trans)} and total value of all transactions is {total}")
cred_trans(jan=1000,feb=2000,mar=3000)

# using both *args and **kwargs
def cred_trans_new(*trans,**info):
    print(trans)
    print(info)
    total = 0
    for i in trans:
        total = total + i 
    print(f"hi {info['name']} you have done {total} amount of transactions ")    
cred_trans_new(1000,2000,3000,name="pranay",email="pranay@gmail.com")

def new_fun(name,**info,):
    pass





      