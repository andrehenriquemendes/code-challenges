class Heap:
    def __init__(self, length):
        self.length = length
        self.arr = [None] * length

    def parent(self, i):
        return int((i - 1) / 2)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def insert(self, value, i):
        self.arr[i] = value
        while self.arr[i] < self.arr[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def get_min(self):
        return self.arr[0]

    def heapify(self, i):
        lower = i

        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.length and self.arr[left] < self.arr[i]:
            lower = left

        if right < self.length and self.arr[right] < self.arr[i]:
            lower = right

        if lower != i:
            self.swap(lower, i)

            self.heapify(lower)

    def delete_root(self):
        self.arr[0] = self.arr[self.length - 1]
        self.arr.pop()
        self.length -= 1

        self.heapify(0)


if __name__ == '__main__':
    arr = [33, 12, 40, 3, 5, 8, 23, 94, 41, 86, 25, 42, 54]

    heap = Heap(len(arr))
    i = 0
    for value in arr:
        heap.insert(value, i)
        i += 1

    print(heap.arr)

    heap.delete_root()

    print(heap.arr)