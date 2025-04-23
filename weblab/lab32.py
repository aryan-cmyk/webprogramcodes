students = []
n = int(input("How many students? "))

for i in range(n):
    name = input("Name: ")
    roll = input("Roll No: ")
    dept = input("Department: ")
    address = input("Address: ")
    gender = input("Gender: ")
    
    marks = []
    for j in range(3):
        m = int(input(f"Enter mark {j+1}: "))
        marks.append(m)
    
    total = sum(marks)
    percent = total / 3

    students.append([name, roll, dept, address, gender, marks, total, percent])

for s in students:
    print("\n--- Student Info ---")
    print("Name:", s[0])
    print("Roll No:", s[1])
    print("Department:", s[2])
    print("Address:", s[3])
    print("Gender:", s[4])
    print("Marks:", s[5])
    print("Total:", s[6], "Percentage:", s[7])

max_s = students[0]
min_s = students[0]
fails = []

for s in students:
    if s[6] > max_s[6]:
        max_s = s
    if s[6] < min_s[6]:
        min_s = s
    for m in s[5]:
        if m < 10:
            fails.append(s[0])
            break

print("\nTopper:", max_s[0])
print("Lowest Scorer:", min_s[0])
print("Fail Students:", fails if fails else "None")
