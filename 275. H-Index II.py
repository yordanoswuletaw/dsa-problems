class Solution:
    def hIndex(self, citations: List[int]) -> int:

        hIndx, n = 0, len(citations)
        low, heigh = 0, n - 1

        while low <= heigh:
            mid = low + (heigh - low) // 2
            # if there is h of n papaer have at least h citations
            if citations[mid] >= (n - mid):
                hIndx = max(n - mid, hIndx)
                heigh = mid - 1
            else:
                low = mid + 1

        return hIndx
