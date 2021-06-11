num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your first number: "))


def greatest(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}!")
    elif num1 < num2:
        print(f"{num2} is greater than {num1}!")


greatest(num1, num2)
