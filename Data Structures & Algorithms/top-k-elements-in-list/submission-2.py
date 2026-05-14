class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        count = Counter(nums)

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [freq for num, freq in heap]
