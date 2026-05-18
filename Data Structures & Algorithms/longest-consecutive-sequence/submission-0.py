class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The idea is like comparing the current element with
        # the next element, if the current element is less than
        # the next element than we increment the total count by 1
        # and keep track of longest the sequence array. If it's nat smaller than
        # the next element, then we remove that element has been added to the array.
        # We keep doing that untile the last element has been checked.
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res