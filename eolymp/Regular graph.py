
import sys
from collections import defaultdict
def main():
    n, m = map(int, sys.stdin.readline().split())
    adjList = defaultdict(list)
    degree = [0] * n 
    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().split())
        adjList[v1].append(v2)
        adjList[v2].append(v1)
        degree[v1 - 1] += 1
        degree[v2 - 1] += 1
    
    if len(set(degree)) <= 1:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
