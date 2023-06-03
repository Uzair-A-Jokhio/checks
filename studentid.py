# this is a child branch 
x = 0
student_name = []
while x <= 4:
    stu = input("enter student name:")
    student_name.append(stu)
    x += 1
print("********************* STUDENT ID *********************")
for i, val in enumerate(student_name):
    print(f"Student ID {i+1}: Name = {val} ")