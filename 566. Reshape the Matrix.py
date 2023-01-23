class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        n, m = len(mat), len(mat[0])
        if n * m != r * c:
            return mat 

        newMat = []
        newRow = []
        
        for i in range(n * m):
             newRow.append(mat[i // m][ i % m])
             if len(newRow) == c:
                newMat.append(newRow)
                newRow = []
        
        return newMat
