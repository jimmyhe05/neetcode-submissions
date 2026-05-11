class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2):
            for x in nums:
                ans.append(x)
        
        return ans

