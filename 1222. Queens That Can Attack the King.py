class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        output = []
        # this loop helps to travers all rows
        for i in [-1,0,1]:
            # this loop helps to travers all columns
            for j in [-1,0,1]:
                if i == j == 0:
                    continue
                row, col = king
                # travers through rows and columns
                while 0 <= row < 8 and 0 <= col < 8:
                    if [row, col] in queens:
                        output.append([row, col])
                        break
                    row += i
                    col += j
        return output

        
        # Check queens in left to king and right to king
        # def checkRow(i, j , k):
        #     res = []
        #     while i >= 0 or k < 8:
        #         if i >= 0 and  [i, j] in queens:
        #             res.append([i, j])
        #             i = -1
        #         else:
        #             i -= 1
        #         if k < 8 and [k, j] in queens:
        #             res.append([k, j])
        #             k = 8
        #         else:
        #             k += 1
        #     return res
        
        # Check queens above and below king
        # def checkColumen(i, j , k):
        #     res = []
        #     while j >= 0 or k < 8:
        #         if j >= 0 and [i, j] in queens:
        #             res.append([i, j])
        #             j = -1
        #         else:
        #             j -= 1
        #         if k < 8 and [i, k] in queens:
        #             res.append([i, k])
        #             k = 8
        #         else:
        #             k += 1
        #     return res
        
        # Check diagonal
        # def checkDiagonal(i, j , k, l):
        #     res = []
        #     while i >= 0 and j>= 0:
        #         if [i, j] in queens:
        #             res.append([i, j])
        #             break
        #         i -= 1
        #         j -= 1

        #     while k < 8 and l < 8:
        #         if [k, l] in queens:
        #             res.append([k, l])
        #             break
        #         k += 1
        #         l += 1
        #     return res

        # Check reverse diagonal
        # def checkReverseDiagonal(i, j , k, l):
        #     res = []
        #     while i >= 0 and j < 8:
        #         if [i, j] in queens:
        #             res.append([i, j])
        #             break
        #         i -= 1
        #         j += 1

        #     while k < 8 and l >= 0:
        #         if [k, l] in queens:
        #             res.append([k, l])
        #             break
        #         k += 1
        #         l -= 1 
        #     return res
        
        # return checkRow(king[0], king[1], king[0]) + checkColumen(king[0], king[1], king[1]) + checkDiagonal(king[0], king[1], king[0], king[1]) + checkReverseDiagonal(king[0], king[1], king[0], king[1])
