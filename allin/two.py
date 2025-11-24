# print("hello world")
name = "Narendra"
age = 20
height = 5.11
is_strudent = True

# print(type(name))
# print(type(age))

# name = input("Enter name: ")
# print(name)

# datatypes
# 1. list
fruit = ["bananas", "oranges"]
fruit.append("pineapple")
fruit.remove("bananas")
fruit[0] = "orange"
# print(fruit)

# print(len(fruit))
# print("orange" in fruit)

#  2. tuple
colors = ("red", "blue", "gree")
# print(colors[1])

# 3. dictionary

person = {
    "name": "Narendra",
    "age": 20,
}


# print(person["name"])
# person["grade"] = "A"
# print(person)
# person["name"] = "Narendra Samtani"
# print(person)

# 4. sets
rollno = {2, 2, 3, 4, 4, 4, 5, 6, 6, 6}
# print(rollno)

# controll flow
age = 10

# if age > 10:
#         print("more than 10")
# elif age == 10:
#         print("equal to 10")
# else:
#         print("less than 10")

# course = ("science", "art", "phycolophy")

# for item in course:
#         print(item)

# for i in range(4):
#         print(i)

# count = 0
# while count < 3:
#         print(count)
#         count += 1

# functions def


def add(num):
    return num + 10


num = 22
# print(add(num))

# string
text = "hello world"

# print(text.lower())
# print(text.upper())
# print(text.split())
# print(text.replace("world", "suckers"))

# file handling
# writing to a file
# with open("example.txt","w") as file:
#         file.write("Hello from tow.py file\n")
#         file.write("this is a test file.")

# with open("example.txt", "r") as file:
#         content = file.read()
#         print(content)


# exception handling

try:
    number = int(input("Enter Int value: "))
    result = 10 / number
    print(result)
except ValueError:
    print("this is not a valid number.")
except ZeroDivisionError:
    print("can not be divided by zero.")
except Exception as e:
    print(f"an error occur {e}")
else:
    print("operation successfull")
finally:
    print("Exectution complete")
