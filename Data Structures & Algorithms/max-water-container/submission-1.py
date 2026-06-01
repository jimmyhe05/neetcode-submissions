class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            min_h = min(heights[l], heights[r])
            dist = r - l
            area = min_h * dist
            if area > max_area:
                max_area = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area

        