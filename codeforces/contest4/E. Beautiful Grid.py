for _ in range(int(input())):
    n = int(input())


    grid = []

    for i in range(n):
        grid.append(list(map(int, input())))
    
    output = 0
    # start and end used as a boundery to traverse the array from outside in
    start, end = 0, n - 1
    while start < end:
        for i in range(start, end):
            rotationSum = grid[start][i] + grid[i][end] + grid[end][end -i + start] + grid[end -i + start][start]
            if rotationSum != 0 and rotationSum != 4:
                output += min(rotationSum, 4 - rotationSum)
        start += 1
        end -= 1

    print(output)
