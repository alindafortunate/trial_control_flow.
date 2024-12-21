age = int(input("Enter your age: "))
user_id = 1245

match age:
    case 18 | 30:
        if age >= 18 and user_id == 245:
            print("You are eligible to vote.")
        else:
            print("You need a user id to be able to vote.")
    case _:
        print("You are not eligible to vote.")
