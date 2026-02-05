grades = {}
n = int(input("How many scores do you want enter?: "))
for i in range(n):
    student_id = int(input("Enter your student id: "))
    score = int(input("Enter your score: "))
    grades[student_id] = score
sorted_items = sorted(grades.items(), key=lambda item: item[1], reverse=True)
if len(sorted_items) == 1:
    print("You just enter one score: ",sorted_items[0])
else:
    second_highest = sorted_items[1] 
    student_id, grade = second_highest
    print(f"شماره دانشجویی: {student_id}, دومین نمره‌ی بزرگ: {grade}")
