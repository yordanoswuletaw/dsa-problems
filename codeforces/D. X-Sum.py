for _ in range(int(input())):
    n, m = map(int, input().split())


    chessboard = [] 
    for _ in range(n):
        chessboard.append(list(map(int, input().split())))

    xSum = float('-inf')

    diagonalSum = {}
    reverseDiagonalSum = {}
    
    for row in range(n):
        for col in range(m):
            diagonalSum[row-col] = diagonalSum.get(row-col, 0) + chessboard[row][col]
            reverseDiagonalSum[row+col] = reverseDiagonalSum.get(row+col, 0) + chessboard[row][col]

    for row in range(n):
        for col in range(m):
            xSum = max(xSum, (diagonalSum[row-col] + reverseDiagonalSum[row+col] - chessboard[row][col]))

    print(xSum)
 
