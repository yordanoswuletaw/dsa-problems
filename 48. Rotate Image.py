class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        base, end = 0, n - 1
        tl = [0,0]
        tr = [0,n-1]
        bl = [n-1, 0]
        br = [n-1, n-1]
       
        while base < end:

            for i in range(base, end):
                matrix[tl[0]][tl[1]], matrix[tr[0]][tr[1]], matrix[br[0]][br[1]], matrix[bl[0]][bl[1]] = matrix[bl[0]][bl[1]],  matrix[tl[0]][tl[1]], matrix[tr[0]][tr[1]], matrix[br[0]][br[1]]
                tl[1] += 1
                tr[0] += 1
                br[1] -= 1
                bl[0] -= 1
            base += 1
            end -= 1
            tl = [base, base]
            tr = [base, end]
            bl = [end, base]
            br = [end, end]

