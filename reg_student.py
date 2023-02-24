from main import Student

try:
    student_name = input("Enter your student name \n")
    student_id = input("Enter your Student ID \n")
    student_stream = input("Enter your Student Stream \n")

    Student.create(stud_name=student_name, stud_id=student_id, stud_stream=student_stream)
    print("Student Created Successfully")

except:
    print("Failed to create student .Use a different email.")
