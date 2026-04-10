age = int(input("Enter your age"))
if age >= 18:
    registered_vote = input("Are you a registered voter? (True/False)")
    registered_vote = registered_vote.lower()
    if registered_vote =="true":
        print("You are eligible to vote.")
    else:
        print("You neet to register to vote.")
else:
    print("You are not eligible to vote.")