# QUICK SORT
def quicksort(arr):
    # Recursion base case
    if len(arr) <= 1:
        return arr    
    # Divide array in two halves around a pivot index (exclusive)
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [pivot] if pivot in arr else []
    right = [x for x in arr if x > pivot]
    # Recursive quick sort of both halves and reassembly of sorted halves
    return quicksort(left) + middle + quicksort(right)

# MERGE SORT
def mergesort(arr):
    # Recursion base case
    if len(arr) <= 1:
        return arr
    # Recursively splitting array in two until left and right are atomic elements
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    # First action of merge() occurs in last recursion expansion, cascading back
    return merge(left, right)

# Does the actual sorting in recursive call stack
def merge(left, right):
    result = []
    i = 0
    j = 0
    # Loops only as long until either left or right half is iterated through
    while i < len(left) and j < len(right):
        # Comparing two numbers, add the smaller number to result list
        # Only shift half when number is chosen from it
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # After one half terminates before the other, add the remainders respectively
    result += left[i:]
    result += right[j:]
    return result

# HEAP SORT
def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)