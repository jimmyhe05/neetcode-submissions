class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subsets = []

        def backtrack(i: int) -> None:
            if len(nums) == i:
                result.append(subsets.copy())
                return

            # include the nums[i]
            subsets.append(nums[i])
            backtrack(i + 1)
            subsets.pop()

            # exclude the nums[i], and skip all its duplicates to avoid duplicate subset
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)

        return result