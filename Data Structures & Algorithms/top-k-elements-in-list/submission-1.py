class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1


        sorted_item = sorted(count.items(), key=lambda x: x[1], reverse=True)

        
        return [num for num, freq in sorted_item[:k]]