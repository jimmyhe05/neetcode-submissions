class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        

        for i in range(len(nums) - k + 1):
            max_i = nums[i]
            for j in range(i, i + k):
                max_i = max(max_i, nums[j])
            res.append(max_i)
        
        return res