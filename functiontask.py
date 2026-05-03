m1 = int (input("Enter the ENG marks: "))
m2 = int (input("Enter the DZO marks:"))
m3 = int (input("Enter the MATH marks:"))
            

def sum_with_return(m1,m2,m3):
    return m1+m2+m3
total =  sum_with_return(m1,m2,m3)
print("The total marks:",total)

def average_with_return(total):
    return total/3
average = average_with_return(total)
print("The average marks is :", average)

if average >= 50 :
     print("Result:PASS")
else :
    print("Result: FAIL")

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"
    
number = int(input("Enter a number:"))
print("The number is:", check_even_odd(number))