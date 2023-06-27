num_1 = float(input("What is your first number? "))
num_2 = float(input("What is you second number? "))
operator = input("What is the operation(+,-,*,/) ")

if operator == "+":
    print(f"Your number is {num_1 + num_2}")
elif operator == "-":
    print(f"Your number i5. {num_1 - num_2}")
elif operator == "*":
    print(f"Your number is {num_1 * num_2}")
else:
    print(f"Your number is {num_1 / num_2}")