class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n

        pref[0] = 1
        suff[n - 1] = 1

        # element to the left of index
        # use ex 1: 1, 1, 2, 8
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]

        # element to the right of index
        # use ex 1: 48, 24, 6, 1
        # i = 0, nums[1] * suff[1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res