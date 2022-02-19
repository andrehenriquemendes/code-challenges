def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, r)
    return i + 1


def quicksort(arr, p, r):
    if p < r:
        pivot = partition(arr, p, r)
        quicksort(arr, p, pivot - 1)
        quicksort(arr, pivot + 1, r)


arr = [12, 33, 34, 1, 3, 55, 3, 677, 34, 33, 5, 98]
if __name__ == '__main__':
    quicksort(arr, 0, len(arr) - 1)

    print(arr)