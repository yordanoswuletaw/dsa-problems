class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:

        arr = sorted(zip(y,x), reverse=True)
        hash_set = set()
        max_sum = 0
        for i, j in arr:
            if j not in hash_set:
                hash_set.add(j)
                max_sum += i
            if len(hash_set) == 3:
                return max_sum
        
        return -1

        