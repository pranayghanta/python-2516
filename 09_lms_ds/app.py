# LMS -> sub feature - student management system
# system information --> Tuples
SYSTEM_INFO = ("LMS Student Portal","v1.0","2025","Edify University")
ADMIN_INFO = ("admin@edify.ai","8355473663","301")
# DISPLAY SYSTEM INFO
print("="*50)
print(F"welcome to {SYSTEM_INFO[0]}")
print(f"Developed by {SYSTEM_INFO[3]}")
print("="*50)

# store all students --> dictionary
students = {}

# start with option selection
while True:
    print("Choose an option from (1-5): ")
    print("1 - add student")
    print("2 - update student")
    print("3 - delete student")
    print("4 - list all students")
    print("5 - exit system")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("performing operation 1")
        student_id = input("Enter student ID: ")
        # student exists
        if student_id in students:
            print("student already with this ID exists in system!")
        else:
            name = input("Enter student name: ").title()
            # store multiple scores
            scores = []   
            while True:
                score_input = input("Enter a score or type done: ")
                # validate if input is number or done
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)   
                    else:
                        print("score should be between 0-100")
                else:
                    print("score should be number only")
            # store multiple unique skills
            skills = set()
            while True:
                skill_input = input("enter a skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input.strip().title())

                # save student details received so far
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }    
            print("student  added successfully!")

            # for verification print student
            print(students)                         
    elif choice == "2":
        print("performing operation 2")  
        student_id = input("Enter student ID to modify: ")
        if student_id in students:
            new_name = input("Enter new name to update: ").title()
            students[student_id]["name"] = new_name
            print("student updated successfully!")
        else:
            print("student ID doesn't exist!") 

        print(students)                         
   
    elif choice == "3":
        print("performing operation 3")
        student_id = input("Enter student ID to delete: ")
        removed = students.pop(student_id,None)
        if removed:
            print("student removed successfully!")
        else:
            print("student ID doesn't exist!")
        print(students)        
    elif choice == "4":
        print("performing operation 4")  
        # id - student_id
        # skills
        # scores
        # students  
        if not students:
            print("No students available")
        else:
            print("="*50)
            print("student details") 
            print("="*50)

            for sid, data in students.items():
                name = data["name"]
                scores = data["scores"]

                if scores:
                    avg = sum(scores)/len(scores)
                else:
                    avg = 0

                if scores:
                    top_score = max(scores)
                else:
                    top_score = 0

                skills = data["skills"]
                print(f"ID: {sid}")
                print(f"name: {name}")
                print(f"scores: {scores}")
                print(f"average score: {avg}")
                print(f"Top score: {top_score}")
                print(f"skills: {skills}")
                print(f"skills count: {len(skills)}")                
                   
    elif choice == "5":
        print("performing operation 5")  
        break  
    else:
        print("invalid choice only (1-5) available")


