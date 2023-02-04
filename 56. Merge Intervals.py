class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals
            
        intervals.sort(key = lambda each: each[0])

        i, j = 0, 1
        mergedIntervals = []
        while j < len(intervals):
            if intervals[i][1] < intervals[j][0]:
                mergedIntervals.append(intervals[i])
                i = j
            else:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
            if j == len(intervals) - 1:
                mergedIntervals.append(intervals[i])
            j += 1

        return mergedIntervals
