#Reading filese in python
f = open("file.txt", 'r')
print(f)
text = f.read()
print(text)
f.close()

# Writing mode
f = open('file.txt', "w")
f.write("Python is a versatile language that can be used for a wide range of applications, \n"
        "from web development and scientific computing to artificial intelligence and machine learning.\n "
        "It has a large and active community of developers, which contributes to the development of libraries,\n "
        "frameworks, and tools that make it easier for developers to solve complex problems.\n")
f.close()

# Open files in write mode
# file = open('file.tx', "a")
# file.write("Python is very easy to understand and its syntax are very easy")
# file.close()


f = open('file.txt', "r")
content = f.read(20)
print(type(content))
print(content)
f.close()

# Reading file through the loop
f = open('file.txt', "r")
for i in f:
    print(i)

# Reading line using readline()
f = open('file.txt', "r")
content = f.readline()
content1 = f.readline()
print(content)
print(content1)
f.close()

# # Creating New file
#
# file = open('fil2.txt', "r")
# print(file)
# if file:
#     print("Created successfully")