def display_menu():
    print("\nDictionary Operations Menu:")
    print("1. Add a key-value pair")
    print("2. Update a value")
    print("3. Delete a key")
    print("4. Check if a key exists")
    print("5. Get value by key")
    print("6. Get all keys")
    print("7. Get all values")
    print("8. Get all items")
    print("9. Clear dictionary")
    print("10. Exit")

def main():
    my_dict = {}  # Initialize an empty dictionary
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
            print("Key-value pair added.")
        
        elif choice == "2":
            key = input("Enter key to update: ")
            if key in my_dict:
                value = input("Enter new value: ")
                my_dict[key] = value
                print("Value updated.")
            else:
                print("Key not found.")
        
        elif choice == "3":
            key = input("Enter key to delete: ")
            if key in my_dict:
                del my_dict[key]
                print("Key deleted.")
            else:
                print("Key not found.")
        
        elif choice == "4":
            key = input("Enter key to check: ")
            print("Key exists." if key in my_dict else "Key not found.")
        
        elif choice == "5":
            key = input("Enter key to get value: ")
            print("Value:", my_dict.get(key, "Key not found."))
        
        elif choice == "6":
            print("Keys:", list(my_dict.keys()))
        
        elif choice == "7":
            print("Values:", list(my_dict.values()))
        
        elif choice == "8":
            print("Items:", list(my_dict.items()))
        
        elif choice == "9":
            my_dict.clear()
            print("Dictionary cleared.")
        
        elif choice == "10":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()

