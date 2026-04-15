num = 10
while num >= 1:
    print(num)
    num -= 1
print("Time's up!")

total = 0
while True:
    num = int(input("Enter a integer(0 to stop): "))
    if num == 0:
        break
    total += num
print("Total sum:",total)

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "1234":
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Incorrect credentials")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account locked")


