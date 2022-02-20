def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def heapify(arr, n, i): # O(logn)
    max = i
    l = left(i)
    r = right(i)

    if l < n and arr[l] > arr[max]:
        max = l

    if r < n and arr[r] > arr[max]:
        max = r

    if max != i:
        swap(arr, max, i)
        heapify(arr, n, max)


def build_max_heap(arr): # O(n*logn)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_extract_max(arr, i):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)


def heapsort(arr):
    build_max_heap(arr) # O(n*logn)

    n = len(arr) 
    result = [None] * n

    while n > 0: # O(n*logn)
        result[n - 1] = heap_extract_max(arr, n - 1) # O(logn)
        n -= 1


arr = [1, 4, 73, 22, 54, 23, 55, 113, 23, 33312, 3434, 42, 94, 3, 12, 91, 18, 2, 1, 1, 2222, 3]

print(arr)
heapsort(arr)
print(arr)
