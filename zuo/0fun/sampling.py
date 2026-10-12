import random


class Solution:

    def reservoir_sampling(self, size:int, n:int)->list[int]:
        # if size < 0 or n < 0:
        #     raise ValueError("size and n must be non-negative")
        if n <= size:
            return list(range(1,n+1))

        nums = list(range(1,size+1))

        for i in range(size+1, n+1):
            if random.random() < size/i:
                nums[random.randrange(size)] = i

        return nums

s=Solution()
print(s.reservoir_sampling(3,5))
print(s.reservoir_sampling(10,17))