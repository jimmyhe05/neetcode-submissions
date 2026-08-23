class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combo = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(combo.copy())
                return 
            if remaining < 0:
                return

            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(i, remaining - nums[i])
                combo.pop()

        backtrack(0, target)
        
        return result