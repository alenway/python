#open a file in read mode
# file1 = open("filehandling.txt")

#read the file content
# read_content = file1.read()
# print(read_content)

# open the file2.txt in write mode
# file2 = open("file2.txt", "w")

# file1.close()

# open th file.txt in write mode
file2 = open("file2.txt", "w")
file2.write("nandri edited\n")

# using with open with
with open("demofile.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)

try:
    file1 = open("demofile.txt", "r")
    read_content = file1.read()
    print(read_content)

finally:
    file1.close()
