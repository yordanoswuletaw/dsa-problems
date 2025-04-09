class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        freq = Counter(nums)
        unique_vals = sorted(freq.keys(), reverse=True)
        if unique_vals[-1] < k:
            return -1
        return len(unique_vals) + (-1 if unique_vals[-1] == k else 0)