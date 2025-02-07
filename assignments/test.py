# tup = (10, 20, 30, 40, 50, 60)

# while True:
#     print("\nSample tupple (10, 20, 30, 40, 50, 60)")
#     print("*** Tuple Operations Menu ***")
#     print("1. Find Length of Tuple")
#     print("2. Find Maximum Element")
#     print("3. Find Minimum Element")
#     print("4. Count Occurrences of an Element")
#     print("5. Find Index of an Element")
#     print("6. Exit")

#     choice = input("Enter your choice (1-6): ")

#     if choice == '6':
#         print("Exiting program. Goodbye!")
#         break

#     elif choice == '1':
#         print("Length of the tuple:", len(tup))

#     elif choice == '2':
#         print("Maximum element:", max(tup))

#     elif choice == '3':
#         print("Minimum element:", min(tup))

#     elif choice == '4':
#         item = input("Enter the element to count: ")
#         try:
#             item = eval(item)
#             print(f"Count of {item}:", tup.count(item))
#         except:
#             print("Invalid input. Please enter a valid number.")

#     elif choice == '5':
#         item = input("Enter the element to find index: ")
#         try:
#             item = eval(item)
#             if item in tup:
#                 print(f"Index of {item}:", tup.index(item))
#             else:
#                 print(f"{item} not found in tuple.")
#         except:
#             print("Invalid input. Please enter a valid number.")

#     else:
#         print("Invalid choice. Please enter a number between 1 and 6.")


# my_dict = {"name": "narendra", "age": 25, "city": "Pune", "course": "Python", "year": 2025}

# while True:
#     print("\nSample dict = {name: narendra, age: 25, city: Pune, course: Python, year: 2025")
#     print("*** Dictionary Operations Menu ***")
#     print("1. Display all Keys")
#     print("2. Display all Values")
#     print("3. Display all Key-Value Pairs")
#     print("4. Get Value by Key")
#     print("5. Remove a Key-Value Pair")
#     print("6. Exit")

#     choice = input("Enter your choice (1-6): ")

#     if choice == '6':
#         print("Exiting program. Goodbye!")
#         break

#     elif choice == '1':
#         print("Keys in dictionary:", list(my_dict.keys()))

#     elif choice == '2':
#         print("Values in dictionary:", list(my_dict.values()))

#     elif choice == '3':
#         print("Key-Value Pairs in dictionary:", list(my_dict.items()))

#     elif choice == '4':
#         key = input("Enter the key to fetch value: ")
#         print(f"Value for '{key}':", my_dict.get(key, "Key not found!"))

#     elif choice == '5':
#         key = input("Enter the key to remove: ")
#         if key in my_dict:
#             removed_value = my_dict.pop(key)
#             print(f"Removed ({key}: {removed_value}) from dictionary.")
#         else:
#             print(f"Key '{key}' not found in dictionary.")

#     else:
#         print("Invalid choice. Please enter a number between 1 and 6.")


# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     vowel_count = {v: 0 for v in "aeiou"}

#     for char in s:
#         if char.lower() in vowel_count:
#             vowel_count[char.lower()] += 1

#     return vowel_count

# user_string = str(input("Enter any string: "))

# result = count_vowels(user_string)

# for vowel, count in result.items():
#     print(f"'{vowel}' appears {count} times")

my_list = [10,11,12,13,14,15,16,17,18]

while True:
    print("\nSample list [10,11,12,13,14,15,16,17,18]")
    print("*** List Operations Menu ***")
    print("1. Append an Element")
    print("2. Insert an Element at a Specific Index")
    print("3. Remove an Element")
    print("4. Pop an Element")
    print("5. Reverse the List")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting program. Goodbye!")
        break

    elif choice == '1':
        element = input("Enter the element to append: ")
        my_list.append(eval(element))
        print("Updated List:", my_list)

    elif choice == '2':
        index = int(input("Enter the index: "))
        element = input("Enter the element to insert: ")
        if 0 <= index <= len(my_list):
            my_list.insert(index, eval(element))
            print("Updated List:", my_list)
        else:
            print("Invalid index!")

    elif choice == '3':
        element = input("Enter the element to remove: ")
        try:
            my_list.remove(eval(element))
            print("Updated List:", my_list)
        except ValueError:
            print("Element not found in the list!")

    elif choice == '4':
        index = input("Enter index to pop (leave empty for last element): ")
        try:
            if index.strip():
                popped_element = my_list.pop(int(index))
            else:
                popped_element = my_list.pop()
            print(f"Popped Element: {popped_element}")
            print("Updated List:", my_list)
        except IndexError:
            print("Invalid index!")

    elif choice == '5':
        my_list.reverse()
        print("Reversed List:", my_list)

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
