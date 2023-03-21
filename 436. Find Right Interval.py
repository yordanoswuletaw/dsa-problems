class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        n, hashMap = len(intervals), {intrval[0]: i for i, intrval in enumerate(intervals)}
        res = [-1] * n

        intervals.sort(key = lambda each: each[0])

        for interval in intervals:   
            val = None
            # performing binary search on sorted intervals to get the minimal right interval
            low, heigh = 0, n - 1
            while low <= heigh:
                mid = low + (heigh - low) // 2
                if intervals[mid][0] >= interval[1]:
                    # store the current interval and its minimum right interval
                    val = (interval[0], intervals[mid][0])
                    heigh = mid - 1
                else:
                    low = mid + 1
            
            if val:
                res[hashMap[val[0]]] = hashMap[val[1]]

        return res
