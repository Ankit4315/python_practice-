'''
6. Write a program to calculate the grade of a student from his marks from the following scheme: 
90 - 100 => Ex 
80 - 90 => A 
70 - 80 => B 
60 - 70 => C 
50 - 60 => D 
<50     => F 
'''
marks = []
def grade():
    for i in range (3):
        mark = int(input(f"enter a {i+1} subject maek :> "))
        marks.append(mark)
    reslut = sum(marks)/3
    return reslut

re = grade()

if re >=90 and re <= 100:
    print("ex")
elif re >= 80 and re < 90:
    print("A")
elif re >= 70 and re < 80:
    print("B")
elif re >= 60 and re < 70:
    print("c")
elif re >= 50 and re < 60:
    print("D")
elif re < 50:
    print("F")
else:
    print("somthing want wrong")