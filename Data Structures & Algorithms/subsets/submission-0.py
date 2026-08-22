class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subsets = []

        def backtrack(i: int) -> None:
            if i == len(nums):
                result.append(subsets.copy())
                return
            
            # include nums[i]
            subsets.append(nums[i])
            backtrack(i + 1)
            subsets.pop()

            # not including nums[i]

            backtrack(i + 1)

        backtrack(0)

        return result
        