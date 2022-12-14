[toc]
# CASE 1

###TimeComplexity가 $N^2$ 인경우

```python
def BubbleSort(arr : list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

TimeComplexity가 $n^2$ 를 가지는 BubbleSort를 정의하였다.

```python
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
```


입력받은 arr을 $n^2$의 *TimeComplexity* 를 가지는 *BubbleSort*를 이용하여 정렬하여 주었다. 
그 후 이중 <span style='color: Blue'>for문</span>을 이용하여 ***target*** 의 값을 가지는 값들의 인덱스를 <span style='color: lightskyblue'>min_index, max_index</span>으로 넣어주고 <span style='color: grey'>target_index</span>라는 값으로 추가해주었다.
그 튜플을 값으로 가지는 <span style="color: coral">Total_index</span>에 *append* 해주었다.
이렇게 하면 arr안에 있는 두 값의 합이 ***target*** 값으로 가지는 것이 여러 개 일지라도 
그 값들을 모두 구할 수 있게 된다.

---

# CASE 2
###TimeComplexity가 $nlogn$ 일 경우

```python
def mergeSort(arr : list) -> list:
    if len(arr) > 1: #arr의 길이가 1개 초과일 경우 계속
        mid = len(arr) // 2 #arr의 중간값 인덱스를 찾기 위해 지정
        left = arr[:mid] # arr에서 중간값까지 left로 지정
        right = arr[mid:] # arr에서 중간값부터 마지막까지 right로 지정

        mergeSort(left) # left값들을 1개 단위로 계속 쪼개어줌
        mergeSort(right) # right값들을 1개 단위로 계속 쪼개어줌

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]: 
                arr[k] = left[i] #arr의 값에 left[i]와 right[j]의 값을 비교하여 넣어줌
                i += 1
            else:
                arr[k] = right[j] #arr의 값에 left[i]와 right[j]의 값을 비교하여 넣어줌
                j += 1

            k += 1
        while i < len(left): # left부터 차례대로 arr에 정렬된 값으로 넣어줌
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr
```

TimeComplexity가 항상 $nlogn$를 가지는 mergeSort를 정의하였다.

```python
def search_matched_sum(arr : list, target : int) -> list:
    arr = mergeSort(arr) #arr을 mergeSort로 정렬
    min_index = ()
    max_index = ()
    target_index = ()
    Total_index = []
    i = 0
    while i < len(arr):
        temp = target - arr[i] # target에서 arr[i]의 값을 빼주어 temp로 지정하여줌
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
```

입력받은 arr을 $nlogn$의 *TimeComplexity*를 가지는 *mergeSort*로 정렬하여주었다. 
그 후 *i* 가 *len(arr)* 보다 작을 동안 <span style='color: pink'>temp</span>라는 값을 ***target*** 에서 arr[i]의 값을 뺀 것으로 지정하여 주었다.
만약 <span style='color: pink'>temp</span>값이 arr에 있다면, arr[i]를 <span style='color: lightskyblue'>min_index</span>, <span style='color: pink'>temp</span>를 <span style='color: lightskyblue'>max_index</span>로 넣어주었다.

그 뒤로는 CASE1 과 같이 <span style='color: grey'>target_index</span>라는 값으로 추가해주었고,
그 튜플을 값으로 가지는 <span style="color: coral">Total_index</span>에 *append* 해주었다.

# CASE 3

### 정렬하지 않는 경우

```python
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
```
arr을 정렬하지 않은 채로 index를 찾아준 후 min_index와 max_index를 비교하여 큰 수를 max_index로 넣어줌으로써 같은 값들의 중복을 제거하여 주었다.




