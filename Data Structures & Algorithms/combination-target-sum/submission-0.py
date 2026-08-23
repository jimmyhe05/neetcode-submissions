class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        comb = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(comb.copy())
                return 
            if remaining < 0:
                return

            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i, remaining - nums[i])
                comb.pop()

        backtrack(0, target)

        return result