'''def factorial(num):
num = int(input("Enter number"))
    print("Number", num)
    print("Factorial", factorial(num))
    if (num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num-1)
#print(factorial(3))'''

'''import math
def factorial(n):
    return (math.factorial(n))
num = int(input("Enter number"))
f = factorial(num)
print("Factorial of ", num, "is", f)'''

'''def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    print(GCD(12,54))'''
'''def GCD(a,b):
    if b!=0:
        return GCD(b, a%b)
    else:
        return a

a = input("Enter a number")
b = input("Enter b number")
print("GCD of given two numbers:", GCD(a,b))
print(GCD)'''

'''def Linear_search(list,n,pointer):
    if pointer>=len(list):
        return -1
    if list[pointer]==n:
        return pointer
    return Linear_search(list,n,pointer+1)
list=[12,23,3,4,5,2]
n=2
i=0
print(Linear_search(list,n,i))'''


'''def binary_search(arr, low, high, x):


	if high >= low:

		mid = (high + low) // 2


		if arr[mid] == x:
			return mid


		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)


		else:
			return binary_search(arr, mid + 1, high, x)

	else:

		return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")'''


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











