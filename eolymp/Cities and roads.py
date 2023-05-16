import sys
from collections import defaultdict
def main():
    n = int(sys.stdin.readline())
    graph = []
    hashSet = defaultdict(int)

    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        graph.append(row)
    
    for i in range(n):
        for j in range(n):
            if i <= j and graph[i][j]:
                hashSet[tuple([i,j])] += 1
            elif graph[i][j]:
                hashSet[tuple([j,i])] += 1
    
    print(len(hashSet))
    
if __name__ == '__main__':
    main()
