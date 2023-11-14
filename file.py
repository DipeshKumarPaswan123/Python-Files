fileptr = open("file1.txt", "r")
print(type(fileptr))
for i in fileptr:
    print(i)
