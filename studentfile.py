file = open('Students.xlsx', 'w')
file.write("Name, ID\n")
file.write("Chimi, 001\n")
file.write("Yangchen, 002\n")
file.write("Yeshi, 003\n")
file.write("Tshering, 004\n")
file.write("Kelzang, 005\n")
file.close()
file = open('Students.xlsx', 'r')
students = file.read()
print(students)
file.close()
searchN = input("Enter a name to search: ")
found = False
with open('Students.xlsx', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print()