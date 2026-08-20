class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
            
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        for i in range(k):
            l = -heapq.heappop(max_heap)

        return l


        