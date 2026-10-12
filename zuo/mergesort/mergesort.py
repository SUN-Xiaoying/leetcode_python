from typing import List


class Solution:
    def sort(self, nums: List[int])->List[int]:

        def mergesort(left:int, right:int):
            if left == right: return
            mid = (left+right)//2
            mergesort(left, mid)
            mergesort(mid+1, right)
            merge(left, mid, right)

        def merge(left:int, mid:int, right:int):
            a, b = left, mid+1
            result=[]
            while a<=mid and b<=right:
                if nums[a]<=nums[b]:
                    result.append(nums[a])
                    a+=1
                else:
                    result.append(nums[b])
                    b+=1

            # Syntax Make Your Life Easier
            #     # Append any remaining elements
            #     result.extend(left[i:])
            #     result.extend(right[j:])
            result.extend(nums[a:mid+1])
            result.extend(nums[b:right+1])
            # while a<=mid:
            #     result.append(nums[a])
            #     a+=1
            # while b<=right:
            #     result.append(nums[b])
            #     b+=1
            for i in range(left, right+1): # Mistake: should be right+1
                nums[i] = result[i-left]


        mergesort(0, len(nums)-1)
        return nums

s= Solution()
print(s.sort([6, 3, 2, 4, 1, 5]))
