def bubble_sort(arr):
    
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

def select_sort(arr):
    
    for i in range(len(arr)):
        min_idx = i
        min_value = 101
        
        for j in range(i, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr

def insert_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(less) + [pivot] + quick_sort(greater)

def solution(array, commands):
    answer = []
    
    for start, end, idx in commands:
        slicing = array[start - 1 : end]
        
        sorting = bubble_sort(slicing)
        # sorting = select_sort(slicing)
        # sorting = insert_sort(slicing)
        # sorting = merge_sort(slicing)
        # sorting = quick_sort(slicing)
        
        answer.append(sorting[idx - 1])
    
    return answer