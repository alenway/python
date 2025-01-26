def menu():
    print("\nMenu")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

def add(a,b):
    return a+b

def substact(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: Divide by zero is not allowed"

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if(choice == "1"):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"Result: {add(a,b)}")

    else:
        print("Invalid choice. Please try again.")

