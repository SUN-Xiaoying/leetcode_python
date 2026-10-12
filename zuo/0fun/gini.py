# https://www.bilibili.com/list/8888480?sid=3509640&oid=786836164&bvid=BV1Q14y1B7DH
import random


class Solution:
    def calculate_gini(self, nums: list[float]) -> float:
        n = len(nums)
        total = sum(nums)

        diff_sum = sum(
            abs(x-y)
            for y in nums
            for x in nums
        )
        return diff_sum / (2*n*total)

    def main_mine(self, n:int, rounds:int) -> float:
        nums = [100]*n
        has_money = [True]*n

        while rounds:
            for i in range(len(nums)):
                if has_money[i]:
                    other =  random.randint(0,n-1)
                    nums[i] = nums[i]-1
                    nums[other] = nums[other]+1
                    if nums[i]<=0:
                        has_money[i] = False
                    if nums[other]>0:
                        has_money[other] = True

            rounds = rounds-1

        return self.calculate_gini(nums)

    def main(self, n:int, rounds: int)->float:
        nums=[100]*n
        for _ in range(rounds):
            has_money = [money > 0 for money in nums]

            for i in range(n):
                if has_money[i]:
                    j = random.randint(0,n-1)
                    nums[i] -= 1
                    nums[j] += 1

        return self.calculate_gini(nums)



s =Solution()
print(s.main(100,1))
print(s.main(100,100))
print(s.main(100,500))


# main_mine
# 0.054952
# 0.124214
#
# 0.06017
# 0.134396

# main
# 0.061978
# 0.128708
