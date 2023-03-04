for _ in range(int(input())):
    n, k = map(int, input().split())
    stripe = input()
 
    i = j = 0
    minCellsNum = float('inf')
    currCellNum = 0
    while j < n:
        if k > 0:
            currCellNum += int(stripe[j] == 'W')
            k -= 1
        else:
            minCellsNum = min(minCellsNum, currCellNum)
            currCellNum += int(stripe[j] == 'W')
            currCellNum -= int(stripe[i] == 'W')
            i += 1
        j += 1
 
    print(min(minCellsNum, currCellNum))
