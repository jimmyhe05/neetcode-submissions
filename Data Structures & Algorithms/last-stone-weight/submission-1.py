class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for i in range(len(stones)):
            heapq.heappush(max_heap, -stones[i])

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if y > x:
                heapq.heappush(max_heap, x - y)

        
        max_heap.append(0)

        return abs(max_heap[0])
            


        # print(max_heap)