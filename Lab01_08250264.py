students_list = [] #List to store std name
students_dict = {} # Dictionary to store std details

#Calling a function to add input name,age,grade
name = input("Enter student name: ")
age = int(input("Enter student age:  "))
grade = int(input("Enter student grade: "))

#Add name and details to list and dictionary
students_list.append(name)
students_dict[name]={"age":age,"grade":grade}#key=name and vale=age,grade

print(f"Student{name}added successfully!")#Printing success message

#Display the current data
print("students list:",students_list)
print("students details:",students_dict)

search_name = input("Enter the name of the student to search: ")#Calling a function to search for a std 

#Check whether the std exists in the dictionary
if search_name in students_dict:
    print(f"Found:{search_name},Age:{Students_dict[search_name]['age']},Grade:{students_dict[search_name]['grade']}")
else:
    print("Students not found.")

remove_name =input("Enter the name of the studemt to remove: ")#Remove operation
#Check whether the students exist before removing
if remove_name in students_dict:
    students_list.remove(remove_name)#Delete from list
    del students_dict[remove_name]#Delete from dictionary
    print(f"Student{remove_name}removed successfully!")
else:
    print("Student not found.")
#Present the updated data
print("Updated Students:",students_list)
print("Updated Student Details:,students_dict")