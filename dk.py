'''age= int(input("enter your age->>>"))
if age >= 18:
    print("you are eligible to vote...")

else:
    print("Sorry! you should wait...")'''

def linear_search(list1, n, key):
    for i in range(0, n):
        if(list1[i] == key ):
            return i
    return -1
list1 = [50,40,30,5,4,9]
key = 30
n = len(list1)
res = linear_search(list1, n, key)
if(res == -1):
    print("Element not found")
else:
    print("Element found at index", res)


