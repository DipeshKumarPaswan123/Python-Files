'''def binary_search(arr, low, high, key):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == key:
            return mid


        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)


        else:
            return binary_search(arr, mid + 1, high, key)

    else:

        return -1


# Test array
arr = [2, 3, 4, 10, 40]
key = 3

# Function call
result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")'''

def binary_search(arr, high, low, key):
    if high >= low:
        mid = (high+low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid-1, key)
        else:
            return  binary_search(arr, mid+1, high, key)
    else:
        return -1

arr = [12,15,21,32,37,48,55]
key = 48
result = binary_search(arr, 0, len(arr) -1, key)

if result != -1:
    print("present", str(result))
else:
    print("Not present")




















































