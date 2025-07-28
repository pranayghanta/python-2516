#Implementation of loops
#while loop

count = 1
while count<=5:
    print(count)
    count+=1

#while True:
  #  print("infinite loop")

#use-case to understand while loop

password = "123"
user_input = ""
while user_input != password:
    user_input = input("Enter Password")
print("Access Granted")

# for loop

string = "pranay"
print(dir(string))
for i in string:
    print(i)
# if num = 10,it is not an iterable object so it gives an error
just_num = 10
print(dir(just_num))
#for i in num:
#print(i)
list_num = [10]
print(dir(list_num))
for i in list_num:
    print(i)

#repeat 10 times in a loop in automatic way rather than manually
for i in range(10):
    print("Hi")     

for i in range(1,10,2):
    print(i)

    #print even numbers from 1-20
i=2
while i<=20:
    print(i)
    i+=2
print("===============")
i=2
while i<=20:
    if i%2 == 0:
        print(i)
    i+=1
#using for loop
i = 2
for i in range(2,21,2):
    print(i)

#nested for loop
for i in range(2,3):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")

#nested while loop
i=1
while i<4:
    j=1
    while j<3:
        print(f"{i} X {j} = {i*j}")
        j+=1
    i+=1    
#jump statements
#break demo

for i in range(5):
    if i == 3:
        break
    print(i)

#continue demo
for i in range(5):
    if i == 3:
        continue
    print(i)

#pass demo
if(5>9):
    pass    
