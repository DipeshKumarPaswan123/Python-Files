# def bubble_sort(arr):
#     size = len(arr)
#     for i in range(size-1):
#         for j in range(size-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# arr = [50,40,20,40]
# print("Original array", arr)
# bubble_sort(arr)
# print("sorted array",arr)


#selection sort

def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(i+1,size):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
arr = [90,40,100,30,20]
print("Original array", arr)
selection_sort(arr)
print("Sorted array", arr)


