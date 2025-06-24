# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

for i in range(6):
    student = int(input(f"enter a marks for {i+1} student:> "))
    marks.append(student)
    
marks.sort()
print(marks)