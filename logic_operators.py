# Exploring * and *, * or * and * not *
high_income = True
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Not Eligible")
else:
    print("Eligible.")

# Expression for a person (is eligible for a loan, if they have a high income, good credit and are not a student.)
if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible.")


# Chaining comparison operators
age = 65
if 18 <= age <= 65:  # Age should be between 18 and 65
    print("Candidate eligible.")
else:
    print("Not eligible.")

# Quiz
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
