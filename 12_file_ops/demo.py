# i have a file on persistent storage

# we have open function

# 1st syntax
#open ("filepath",mode)
  # mode - rwa
# read mode
file = open("file.txt","r")
# print(type(file))
print(file)  
print(file.closed)
file.close()
print(file.closed)


# 2nd syntax --> recommended
# with open("filepath",mode)
# mode - rwa
with open("file.txt","r") as file_new:
   # print(type(file_new))
    print(file_new)
   # print(file_new.read()) # closes the connection

   # for character in file_new.read(): # character by character
    #  print(character)
    # read line by line
    # print(file_new.readline())
    # print(file_new.readline())

   # print(file_new.readlines()) # read all lines
    for line in file_new.readlines():
      print(line)

# print(file_new.closed)

# create files -> using write (w) mode
# default behavior is overwrite
# write mode
with open("new.txt","w") as file_new:
    # print(file_new)
    file_new.write("welcome to java \n")
    file_new.write("welcome to python \n")
    file_new.write("welcome to git")

with open("data.txt","w") as file_new:
    # print(file_new)
    file_new.writelines(["welcome to java \n","welcome to python \n","welcome to git \n"])

# append mode --> add to existing data without overwrite
with open("data.txt","a") as file_new:
    # print(file_new)
    file_new.writelines(["welcome to cloud \n","welcome to devops \n","welcome to DS"])

# delete a file
# os module
import os
os.remove("data.txt")






