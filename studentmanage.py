students = []

while True:
    name = input("Enter student name: ")

    marks1 = int(input("Enter marks in Subject 1: "))
    marks2 = int(input("Enter marks in Subject 2: "))
    marks3 = int(input("Enter marks in Subject 3: "))

    students.append([name, marks1, marks2, marks3])

    choice = input("Do you want to add another student? (yes/no): ")

    if choice.lower() == "yes":
        continue

    elif choice.lower() == "no":
        break

    else:
        print("Invalid input")
        break

print("\nNumber of students:", len(students))
print("\nStudent Details:")

for student in students:
    print("Name:", student[0])
    print("Subject 1:", student[1])
    print("Subject 2:", student[2])
    print("Subject 3:", student[3])
    print()