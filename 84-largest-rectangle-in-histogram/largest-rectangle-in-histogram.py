class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        stack = []
        max_area = 0
        for i in range(n):
            height = heights[i]
            curr_indx = i
            while stack and stack[-1][1] > height:
                prev_indx, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (i - prev_indx))
                curr_indx = prev_indx
            stack.append((curr_indx, height))
            
        while stack:
            prev_indx, prev_height = stack.pop()
            max_area = max(max_area, prev_height * (n - prev_indx))

        return max_area
        