class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        merged_intervals = []
        curr_start, curr_end = intervals[0][0], intervals[0][1]
        for start, end in intervals[1:]:
            if curr_end >= start:
                curr_end = max(curr_end, end)
            else:
                merged_intervals.append([curr_start, curr_end])
                curr_start, curr_end = start, end
                
        merged_intervals.append([curr_start, curr_end])
        return merged_intervals
