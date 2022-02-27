# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Heap:

    def __init__(self, length):
        self.length = length
        self.arr = [None] * length

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def parent(self, i):
        return int((i - 1) / 2)

    def insert(self, value, i):
        self.arr[i] = value
        while self.arr[i] > self.arr[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def get_max(self):
        return self.arr[0]

    def heapify(self, i):
        largest = i

        # get children
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.length and self.arr[left] > self.arr[largest]:
            largest = left

        if right < self.length and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.swap(largest, i)
            self.heapify(largest)

    def delete_max(self):
        self.arr[0] = self.arr[self.length - 1]  # replace by the last element on the tree
        self.arr.pop()
        self.length -= 1

        self.heapify(0)


class Solution(object):
    def findKthLargest(self, nums, k):
        heap = Heap(len(nums))

        for i, value in enumerate(nums):
            heap.insert(value, i)

        k = k - 1
        for i in range(k):
            heap.delete_max()

        return heap.get_max()


sol = Solution()
x = sol.findKthLargest([3,2,1,5,6,4], 1)
print(x)