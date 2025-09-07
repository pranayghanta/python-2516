class Student:
    # characteristics / data/ variables / attributes
    student_name = "pranay"
    student_email = "pranay@gmail.com"

    # special method __init__ (constructor)
    def __init__(self,student_name,student_email):
        self.student_name = student_name # instance variable
        self.student_email = student_email # instance variable
    # my custom methods --> instance method
    def info(self):
        print("Student Name: ", self.student_name)
        print("Student Email: ",self.student_email)    

student_one = Student("rana","rana@gmail.com")  
student_second = Student("ran","ran@gmail.com")  
student_third = Student("ghanta","ghanta@gmail.com")
student_one.info()
student_second.info()
student_third.info()

# Student.info(self)

     # method
    #def info(self):
       # print(Student.student_name,Student.student_email) # --> valid
     #   print(self.student_name,self.student_email)
# student_one = Student()
# student_one.info()  

# student_second = Student()
# student_second.info()  

# student_third = Student()
# student_third.info()  




