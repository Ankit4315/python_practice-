# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user
marks = []
def passfail():
    for i in range(3):
        put = int(input(f"inter {i} subject marks :> "))
        marks.append(put)
    result = sum(marks)/3
    return result

result = passfail()
print(result)
print(marks)
if(result >= 40 and marks[0]>=33 and marks[1]>=33 and marks[2]>= 33):
    print("pass",result)
else:
    print("fail",result)