# A program to match data types.
value = input("Enter a value (number or string): ")

match value:
    case int():
        print("You entered an integer:", value)
    case str():
        print("You entered a string:", value)
    case _:
        print("Invalid data type entered.")

# if/else alternative.

entered_value = input("Enter a value (number or string): ")
if type(entered_value) == type(int()):
    print("You entered an integer:", value)
elif type(entered_value) == type(str()):
    print("You entered a string:", value)
else:
    print("You entered an incorrect value.")
age =23

