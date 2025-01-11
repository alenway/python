# implesit type conversion
X = 10
X = "name"

print(X)

Y = 10
Z = 3.4
result = Y + Z

print(result)
print(type(result))

# Explicit type conversion

num_str = "100"
num_str = int(num_str)
print(num_str)
print(type(num_str))

# Convert integer to string
num = 50
num_str = str(num)
print(num_str)  # Output: "50"
print(type(num_str))  # Output: <class 'str'>

# Convert float to integer
flt = 5.67
flt_to_int = int(flt)
print(flt_to_int)  # Output: 5 (decimal part is truncated)

# Convert list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# Convert string to float
flt_num = float("123.45")
print(flt_num)  # Output: 123.45
