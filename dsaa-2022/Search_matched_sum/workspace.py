import random
#n log n인 경우
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
    min_index = ()
    max_index = ()
    target_index = ()
    Total_index = []
    i = 0
    while i < len(arr):
        temp = target - arr[i]
        if temp in arr[arr.index(arr[i]):]:
            min_index = arr.index(arr[i])
            max_index = arr.index(temp)
            target_index = (min_index, max_index)
            if target_index not in Total_index:
                Total_index.append(target_index)
            i += 1
        
        else:
            i += 1
    
    return Total_index
    
    
    
        

arr = []
for _ in range(100):
    arr.append(random.randint(1, 100))


# print(bubbleSort(arr))

result = search_matched_sum(arr, 6)

print(result) 
# (2, 3)