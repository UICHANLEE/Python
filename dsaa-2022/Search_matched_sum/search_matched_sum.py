# n square -> Bubble_Sort
def bubbleSort(arr : list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def search_matched_sum(arr : list, target : int) -> list:
    
    arr = bubbleSort(arr)# 위에서 정의한 BubbleSort를 이용하여 정렬
    
    min_index = () # min_index의 값을 넣어줌
    max_index = () # max_index의 값을 넣어줌
    target_index = () # 조건을 만족하는 값들의 index 값을 저장할 튜플
    Total_index = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr.index(arr[i]) < arr.index(arr[j]):# 정렬해준 리스트에서 index값이 작을 경우만 탐색
                if arr[i] + arr[j] == target:  # arr리스트에 있는 값들 중 두 값을 더한 것이 target과 같을 경우
                    min_index = (arr.index(arr[i]))
                    max_index = (arr.index(arr[j]))
                    target_index = (min_index, max_index)
                    if target_index not in Total_index: # 중복된 값이 있는경우 제외
                        Total_index.append(target_index)
                    else:
                        continue
   
    return Total_index

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
    value_index = ()
    Total_index = []
    
        
def search_matched_sum(arr : list, target : int) -> list:
    min_index = ()
    max_index = ()
    target_index = ()
    Total_index = []
    for i in range(len(arr)):
        temp = target - arr[i]
        if temp in arr:
            min_index = arr.index(arr[i])
            max_index = arr.index(temp)
            if min_index > max_index:
                t = min_index
                min_index = max_index
                max_index = t
            target_index = (min_index, max_index)
            if target_index not in Total_index:
                Total_index.append(target_index)
            continue
        else:
            continue

    return Total_index


arr = [5, 4, 2, 1,1,2,4,5]

# print(bubbleSort(arr))

result = search_matched_sum(arr, 6)

print(result) 
# (2, 3)