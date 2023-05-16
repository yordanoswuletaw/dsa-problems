import sys
from collections import defaultdict
def main():
    n = int(sys.stdin.readline())
    adjMat = [[0 for _ in range(n)] for _ in range(n)]
    adjList = []

    for _ in range(n):
        adjList.append(list(map(int, sys.stdin.readline().split())))
    
    for i, each in enumerate(adjList):
        for j in range(1, len(each)):
            adjMat[i][each[j] - 1] = 1
    
    for row in adjMat:
        print(*row)

    
if __name__ == '__main__':
    main()
