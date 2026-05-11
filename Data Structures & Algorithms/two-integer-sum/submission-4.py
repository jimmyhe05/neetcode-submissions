class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in d and d[diff] != i:
                return [i, d[diff]]