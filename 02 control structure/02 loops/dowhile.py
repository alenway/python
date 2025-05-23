# Python does not have a built-in do...while loop like C, C++, or Java.
# In Python, if you want the same effect, you usually simulate it using a while True loop with a break. Here’s how you do it:

while True:
    # do something
    user_input = input("Enter 'yes' to continue: ")
    if user_input != "yes":
        break
