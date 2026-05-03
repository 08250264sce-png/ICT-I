def sum():
    a = 5
    b = 10
    print("The sum of a and b is:", a + b)

def product():
    a = 5
    b= 10
    print("The product of a and b is:", a * b)

# sum()
# product()

def sum_with_parameters(x,y):
    print("The sum of", x, "and", y, "is:", x + y)
sum_with_parameters(3, 7)

def product_with_parameters(x,y):
    print("The product of", x, "and", y, "is:", x * y)
product_with_parameters(3, 7)

def sum_with_return(x, y):
    return x + y
print("The sum of 4 and 6 is:", sum_with_return(4, 6))

def product_with_return(x, y):
    return x * y
print("The product of 4 and 6 is:", product_with_return(4, 6))


def sum():
    sub1 = 66
    sub2 = 60
    sub3 = 75
    print("The sum of sub1, sub2 and sub3 is:", sub1 + sub2 + sub3 ) 

sum()

def average():
    sub1 = 66
    sub2 = 60
    sub3 = 75
    print("The average of sub1, sub2 and sub3 is:",(sub1 + sub2 + sub3 /3))

average()

def average_with_return(sub1,sub2,sub3):
    return sub1 + sub2 + sub3
print("The average of sub1, sub2 and sub3 is:", average_with_return(sub1, sub2, sub3 /3))
