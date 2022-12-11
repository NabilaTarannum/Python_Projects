print("Welcome to Calculator")
first_number = int(input("Enter your first number :"))
last_number = int(input("Enter your last number :"))
operation = input("Enter a sign :")

if operation == "+":
    print(first_number + last_number)
elif operation == "-":
    print(first_number - last_number)
elif operation == "*":
    print(first_number * last_number)
elif operation == "/":
    print(first_number / last_number)
elif operation == "**":
    print(first_number**last_number)
elif operation == "//":
    print(first_number // last_number)
elif operation == "%":
    print(first_number % last_number)
else:
    print("Invalid operation")
