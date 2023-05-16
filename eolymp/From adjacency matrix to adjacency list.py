import sys
from collections import defaultdict
def main():
    n = int(sys.stdin.readline())
    graph = []
    adjList = defaultdict(list)

    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        graph.append(row)
    
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                adjList[i].append(j + 1)
    
    for key, value in adjList.items():
        print(len(value), *value)
    
if __name__ == '__main__':
    main()
