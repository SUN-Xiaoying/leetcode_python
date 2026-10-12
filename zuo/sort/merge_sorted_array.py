# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
from typing import List


class Solution:
    # Input:
    # [1, 2, 4, 5, 6, 0]
    # 5
    # [3]
    # 1
    # Output:
    # [1, 2, 3, 5, 6, 4]
    # Expected:
    # [1, 2, 3, 4, 5, 6]
    def merge_wrong(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        head: int = 0
        tail: int = m
        nums2_pointer: int = 0
        while nums2_pointer < len(nums2):
            if nums1[head] > nums2[nums2_pointer]:
                nums1[tail] = nums1[head]
                nums1[head] = nums2[nums2_pointer]
                nums2_pointer += 1
                tail += 1
                head += 1
            elif head < m:
                head += 1
            else:
                nums1[tail] = nums2[nums2_pointer]
                tail += 1
                nums2_pointer += 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m-1
        p2 = n-1
        p = m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2-=1
            else:
                nums1[p] = nums1[p1]
                p1-=1
            p -= 1

        # not consider p1>=0, for nums1[0..m-1] is already in place and sorted
        while p2>=0:
            nums1[p] = nums2[p2]
            p-=1
            p2-=1


if __name__ == "__main__":
    sol = Solution()
    # nums1:List[int] = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3

    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5
    sol.merge(nums1, m, nums2, n)
    print(nums1)