
from typing import List

class Solution:
    def heap_sort(self, arr:List[int]):
        for i in range(arr):
            self.heap_insert(arr, 1)
        print(arr)


    # TODO：从底到顶
    def heap_insert(self, arr: List[int], i: int):
        while (arr[(i - 1) / 2] > arr[i]):
            # What if i==0
            # (0-1)/2 == -0.5
            arr[(i - 1) / 2], arr[i] = arr[i], arr[(i - 1) / 2]
            i = (i - 1) / 2


    # TODO：从顶到底
    def heapify(self, arr: List[int], i: int, size:int):
        l = i*2+1
        while l<size:
            best = l+1 if l+1<n and arr[l+1]>arr[l] else l
            if arr[i] > arr[best]:
                arr[i], arr[best] = arr[best], i
                i = best
                l = i*2 + 1
            else: break

s = Solution()

print((0-1)//2)