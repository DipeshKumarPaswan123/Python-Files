'''for i in range(20000):
    print(i+ 1)'''

"""fruits = "Apple", "Mango", "Grapes "
for fruit in fruits:
  print(fruit)
  for i in fruits:
    print(i)
    ##print("I love this one")"""

#for a in range(1, 30, 3):
    #print(a+ 1)

#Table of n numbers

'''n = int(input("Enter number"))
for i in range(1, 11):
    print(n, 'x', i, '=', n*i)'''


def linear_Search(list1, n, key):
    # Searching list1 sequentially
    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1


list1 = [1, 3, 5, 4, 7, 9]
key = 7

n = len(list1)
res = linear_Search(list1, n, key)
if (res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)





