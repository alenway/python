# range()
print(list(range(1,5)))

# enumerate()
for i, v in enumerate(["a","b","c"]):
    print(i,v)

# zip()
name = ["nitin","ravi"]
ages = [20,21]
print(list(zip(name,ages)))

# map()
nums = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x*2, nums)))


# filter()
print(list(filter(lambda x: x % 2 == 0, nums)))
