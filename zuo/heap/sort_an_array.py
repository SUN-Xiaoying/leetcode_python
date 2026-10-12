# https://leetcode.com/problems/sort-an-array/?envType=problem-list-v2&envId=heap-priority-queue
from heapq import heapify
from typing import List


def swap(arr:List[int], i:int, j:int):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


class Solution:
    # O(nlog(n)) time complexity
    # Without using any built-in functions

    # MaxHeap, A max-heap gives the largest element first.
    def heap_insert(self, arr: List[int], i:int):
        while i>0 and arr[(i-1)//2] < arr[i]:
            swap(arr, (i-1)//2, i)
            i = (i-1)//2

    def heapify(self, arr: List[int], i:int, size:int):
        l= i*2 + 1
        while l<size:
            best = l+1 if l+1 <size and arr[l+1]>arr[l] else l # MinHeap, Choose the smaller one
            if arr[best] > arr[i]:
                swap(arr, best, i)
                i=best
                l=i*2+1
            else: break

    # 1015 ms Beats 6.49%
    # 从顶到底
    def sortArray1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            self.heap_insert(nums, i)
        for i in range(n-1, 0, -1):
            swap(nums, 0, i)
            self.heapify(nums, 0,i)
        return nums

    # 从底到顶
    # 899 ms Beats 10.80%
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # for i in range(n - 1, 0, -1):
        #     self.heapify(nums, i, n)
        # You should not start from n-1 (the last leaf node). You must start from the last parent node, which is at index (n // 2) - 1
        start_index = (n // 2) - 1
        for i in range(start_index, -1, -1):
            self.heapify(nums, i, n)
        print("MaxHeap: ", nums)
        for i in range(n-1, 1, -1):
            swap(nums, 0, i)
            self.heapify(nums, 0,i)
        return nums


s = Solution()
# print(s.sortArray([5,1,1,2,0,0]))

# [-7,-5,-4,-1,-1,0,0,4,7,9]
print(s.sortArray([-4,0,7,4,9,-5,-1,0,-7,-1]))