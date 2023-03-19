class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        nums.sort()
        low, heigh = 1, nums[-1]
        smDivider = heigh

        while low <= heigh:
            mid = low + (heigh - low) // 2
            res = sum(map(lambda e: ceil(e/mid), nums))
           
            if res <= threshold:
                smDivider = min(smDivider, mid)
                heigh = mid - 1
            else:
                low = mid + 1
        
        return smDivider
