print("""
- for the subtraction
+ for the addation
/ for the division
* for the multiplicatoin
""")

number1 = int(input("Enter your first number: "))
number2= int(input("Enter your second number: "))
operator = input("Enter your operator for your calculation: ")
if(operator == "-"):
    print(number1-number2)
elif(operator == "+"):
    print(number1+number2)
elif(operator == "/"):
    print(number1/number2)
elif(operator == "*"):
    print(number1*number2)
else:
    print("Operation that you give is invalid")