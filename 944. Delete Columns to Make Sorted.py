class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        notSortedCols = 0
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                if strs[row-1][col] > strs[row][col]:
                    notSortedCols += 1
                    break 

        return notSortedCols
