num1 = input("Enter the fist number ")
num2 = input("Enter the second number ")
operation = input("Enter the operation ")

if operation == '+':
    print(int(num1) + int(num2))
elif operation == '-':
    print(int(num1) - int(num2))
elif operation == '*':
    print(int(num1) * int(num2))
elif operation == '/':
    print(int(num1) / int(num2))
elif operation == '%':
    print(int(num1) % int(num2))
else:
    print("operation invalid")