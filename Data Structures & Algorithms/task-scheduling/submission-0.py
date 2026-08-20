from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]  # negate for max-heap
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()  # holds (remaining_count, time it becomes available again)

        while max_heap or cooldown:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # run one instance (cnt is negative)
                if cnt != 0:
                    cooldown.append((cnt, time + n))

            if cooldown and cooldown[0][1] == time:
                cnt, _ = cooldown.popleft()
                heapq.heappush(max_heap, cnt)

        return time