import sys
from collections import defaultdict
def main():
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())

    ans = []
    graph = defaultdict(list)
    for i in range(k):
        input = list(map(int, sys.stdin.readline().split()))
        if input[0] == 1:
            graph[input[1]].append(input[2])
            graph[input[2]].append(input[1]) 
        else:
            print(*graph[input[1]])
    
if __name__ == '__main__':
    main()
