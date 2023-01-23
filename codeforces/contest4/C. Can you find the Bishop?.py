for _ in range(int(input())):
    matrix = []
    input()
    for i in range(8):
        row = list(input())
        matrix.append(row)
   
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                if 0 < i < 7 and 0 < j < 7:
                    if matrix[i-1][j-1] == matrix[i-1][j+1] == '#':
                        print(i + 1, j + 1)
                        break   
