# this is a child branch 
q = 5
x = 0
student_name = []
while x <= q:
    stu = input(
        f"Enter Student name \n "
         f"Name:  ")
    student_name.append(stu)
    x += 1
print("********************* STUDENT ID *********************")
for i, val in enumerate(student_name):
    print(f"Student ID {i+1}: Name = {val} ")
