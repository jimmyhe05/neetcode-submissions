class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for i in range(len(points)):
            dist = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            heapq.heappush(max_heap, (-dist, points[i][0], points[i][1]))

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        return [[x, y] for dist, x, y in max_heap]

        