from main import Student

mystudents = Student.select()
for student in mystudents:
    print(student.name, student.id, student.stream)
