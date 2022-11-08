# # n square -> Bubble_Sort
# def bubbleSort(arr : list) -> list:
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr


# def search_matched_sum(arr : list, target : int) -> list:
#     arr = bubbleSort(arr) 
#     min_index = ()
#     Total_index = []
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr.index(arr[i]) < arr.index(arr[j]):
#                 if arr[i] + arr[j] == target:
#                     min_index = (arr.index(arr[i]), arr.index(arr[j]))
#                     if min_index not in Total_index:
#                         Total_index.append(min_index)
#                     else:
#                         continue
   
#     return Total_index

# n log n인 경우
def mergeSort(arr : list) -> list:
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        print(arr)
        print(left)
        print(right)

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

def search_matched_sum(arr : list, target : int) -> list:
    arr = mergeSort(arr)
    start = 0
    end = len(arr)
    value_index = ()
    Total_index = []
    if arr[start] + arr[end] == target:
        


arr = [5, 4, 2, 1,1,2,4,5]

# print(bubbleSort(arr))

result = mergeSort(arr)

print(result) 
# (2, 3)