def main():
    print("!CALCULATOR!")
print("Enter numbers")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter last number:"))

choice = int(input("Which sum would you like to Calculate? Enter 1, 2, or 3:"))

if choice == 1:
    result = num1 + num2
    print("ADDITION", result)

if choice == 2:
    result = num1 - num2
    print("SUBTRACTION",result)

if choice == 3:
    result = num1 / num2
    print("DIVISION",result)

if choice == 4:
    result = num1 * num2
    print("MULTIPLICATION",result)

if choice == 5:
    result = num1 % num2
    print("PERCENTAGE",result)

