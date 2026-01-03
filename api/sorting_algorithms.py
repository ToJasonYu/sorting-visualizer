def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            yield arr, list(range(n-i, n)), [j, j+1]
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr, list(range(n-i, n)), [j, j+1]
                
    yield arr, list(range(n)), []

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            yield arr, list(range(0, i)), [min_idx, j]
            if arr[j] < arr[min_idx]:
                min_idx = j
                yield arr, list(range(0, i)), [min_idx, j]
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr, list(range(0, i+1)), [i, min_idx]
        
    yield arr, list(range(n)), []

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            yield arr, [], [j, j+1]
            arr[j + 1] = arr[j]
            j -= 1
            yield arr, [], [j, j+1]
        arr[j + 1] = key
        yield arr, [], [j+1]
        
    yield arr, list(range(len(arr))), []

def quick_sort(arr, low, high):
    locked = []
    yield from _quick_sort_recursive(arr, low, high, locked)
    yield arr, list(range(len(arr))), []

def _quick_sort_recursive(arr, low, high, locked):
    if low < high:
        pi = yield from partition(arr, low, high, locked)
        if pi not in locked:
            locked.append(pi)
            yield arr, list(locked), [pi] 
            
        yield from _quick_sort_recursive(arr, low, pi - 1, locked)
        yield from _quick_sort_recursive(arr, pi + 1, high, locked)
    elif low == high:
        if low not in locked:
            locked.append(low)
            yield arr, list(locked), [low]

def partition(arr, low, high, locked):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        yield arr, list(locked), [j, high]
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr, list(locked), [i, j]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr, list(locked), [i+1, high]
    return i + 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        yield from merge_sort(arr, left, mid)
        yield from merge_sort(arr, mid + 1, right)
        yield from merge(arr, left, mid, right)
    
    if left == 0 and right == len(arr) - 1:
        yield arr, list(range(len(arr))), []

def merge(arr, left, mid, right):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]
    i = 0
    j = 0
    k = left
    while i < len(left_copy) and j < len(right_copy):
        yield arr, [], [k]
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1
    while i < len(left_copy):
        yield arr, [], [k]
        arr[k] = left_copy[i]
        i += 1
        k += 1
    while j < len(right_copy):
        yield arr, [], [k]
        arr[k] = right_copy[j]
        j += 1
        k += 1

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(arr, n, i, [])
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        locked = list(range(i, n))
        yield arr, locked, [0, i]
        yield from heapify(arr, i, 0, locked)
    yield arr, list(range(n)), []

def heapify(arr, n, i, locked):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    yield arr, locked, [i] 

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield arr, locked, [i, largest]
        yield from heapify(arr, n, largest, locked)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            yield arr, [], [i, j - gap] 

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                yield arr, [], [j, j - gap]
                j -= gap
            
            arr[j] = temp
            yield arr, [], [j]

        gap //= 2

    yield arr, list(range(n)), []


def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while (swapped == True):
        swapped = False

        for i in range(start, end):
            yield arr, list(range(n-1, end, -1)) + list(range(0, start)), [i, i+1]
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                yield arr, list(range(n-1, end, -1)) + list(range(0, start)), [i, i+1]

        if (swapped == False):
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            yield arr, list(range(n-1, end, -1)) + list(range(0, start)), [i, i+1]
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                yield arr, list(range(n-1, end, -1)) + list(range(0, start)), [i, i+1]

        start = start + 1

    yield arr, list(range(n)), []

def gnome_sort(arr):
    n = len(arr)
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        
        if arr[index] >= arr[index - 1]:
            yield arr, [], [index, index - 1] 
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            yield arr, [], [index, index - 1]
            index = index - 1

    yield arr, list(range(n)), []

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    n = len(arr)

    while max1 // exp > 0:
        yield from counting_sort_for_radix(arr, exp)
        exp *= 10
    
    yield arr, list(range(n)), []

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = (arr[i] // exp)
        yield arr, [], [i]
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]
        yield arr, [], [i]