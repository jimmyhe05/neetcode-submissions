class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        

        for right in range(len(nums) - k + 1):
            max_num = float('-inf')
            
            for num in range(left, k + left):
                if nums[num] > max_num:
                    max_num = nums[num]
            res.append(max_num)
            left += 1
        
        return res