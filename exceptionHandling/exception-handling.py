#Regular division example
#result=10/0
#print(result)
#Displays built-in exceptions
# print(dir(locals()['__builtins__']))
#Exception Handling in Python
# try:
#     num = 10
#     denom = 0

#     divresult = num/denom

#     print(divresult)
# except:
#     print("Denominator cannot be 0")
#finally block
# try:
#     num = 10
#     denom = 0
#     result = num/denom
#     print(result)
# except:
#     print("Denominator cannot be 0")
# finally:
#     print("This is finally block")

#Using more than one except block for handling
#specific exceptions
# try:
#     # ndiv=12/0
#     # print(ndiv)
#     num = [1,2,3,4,5]
#     print(num[5])
# except ZeroDivisionError:
#     print("Denominator cannot be 0")
# except IndexError:
#     print("Index is Out of Bound")

# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    num % 2 == 1
except:
    print("The entered number is even")
else:
    print("The entered number is odd")

# User-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the age is less than 18"
#     pass
# age = 18
# try:
#     input_age = int(input("Enter a age: "))
#     if input_age < age:
#         raise InvalidAgeException
#     else:
#         print("You can vote")

# except InvalidAgeException:
#     print("Invalid Age")
