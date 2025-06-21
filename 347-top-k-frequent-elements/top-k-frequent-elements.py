class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
        
        most_frequent_nums = []
        while k > 0:
            _, num = heapq.heappop(heap)
            most_frequent_nums.append(num)
            k -= 1
        
        return most_frequent_nums