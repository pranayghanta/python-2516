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

# working with csv files
# read data
import csv
with open("sample_data.csv","r") as file_data:
  csv_reader = csv.reader(file_data)
  print("Data")
  print(csv_reader)
  for row in csv_reader:
      if row[3] == "hyderabad":
        print(row)
    # print(row)
# get the customers from hyderabad --> first priority ship products to hyd customers
    # print("Hyderabad Customers")
    # print(row)
    # if row[3]=="hyderabad":
    #   print(row)
# get the customers for gmail --> first priority ship products to hyd customers
      if row[1].endswith("@gmail.com"):
        print(row)

# DictReader --> gives the dictionary object
with open("sample_data.csv","r") as file_data:
  csv_reader = csv.DictReader(file_data)
  print(csv_reader)
  for row in csv_reader:
    if row["email"].endswith("@gmail.com"):
      print(row)


# now writing the data
with open("write_data.csv","w") as file_data:
  csv_writer = csv.writer(file_data)
  csv_writer.writerow(['name','email','mobile','location'])
  csv_writer.writerow(['pranay','pranay@gmail.com','735767364','hyderabad'])
  csv_writer.writerows([['pranay','pranay@gmail.com','735767364','hyderabad'],['ghanta','ghanta@gmail.com','87465474','pune']])

# now appending the data
with open("write_data.csv","a") as file_data:
  csv_writer = csv.writer(file_data)
  csv_writer.writerows([['user1','user1@gmail.com','735767364','hyderabad'],['user2','user2@gmail.com','87465474','pune']])


# working with json data
import json
student = {
  "id": 101,
  "name": "pranay",
  "course": "python full strack",
  "skills": ["python","git","aws"],
  "score": 90
}
print(type(student))
# now writing the data
with open("student.json","w") as file_data:
  json.dump(student,file_data,indent = 4)

# now read the data
with open("student.json","r") as file_data:
  json_data = json.load(file_data)
  print(json_data)
  print(type(json_data))
  print(json_data['name'])
  print(json_data['skills'][0])

# ops betwen json & python data 
# convert python json data to string data
student_json = json.dumps(student)
print(student_json)

# convert string data to json
json_string = '{"id": 102,"name": "ghanta","course":"data science"}'
print(type(json_string))
stu_data = json.loads(json_string)
print(stu_data)
print(type(stu_data))














