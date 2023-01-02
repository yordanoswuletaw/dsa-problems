n = int(input())
for i in range(n):
    colorLen, currColor = input().split()
    colors = input()

    minSec = currSec = 0
    for i, color in enumerate(colors):
        if not currSec and color != currColor:
            continue
        else:
            if color == 'g':
                minSec = max(currSec, minSec)
                currSec = 0
            elif i == int(colorLen) - 1:
                currSec += 1
                j = 0
                while colors[j] != 'g':
                    j += 1
                    currSec += 1
            else:
                currSec += 1
    print(max(currSec, minSec))
