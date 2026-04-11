student_name = input("Enter name:")
days_borrowed = int(input("How many day it have been since you borrowed the book from libary?:"))
days_late = int(input("How many days late have you returned the book?"))
if(days_late == 0):
    print("no need for fine")
elif(days_late >=1 and days_late <=5):
    print("nu.5 per day")
elif(days_late >=6 and days_late <=9):
    print("nu.10 per day")
else:
    print("nu.20 per day")
if(days_borrowed >30):
    print("WARNING!libary privilege may be restricted")
else:
    print("")
                      
                      

