import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()


def runCases():
    n = int(input())
    p = list(map(int, input().split()))
    
    adjMap, root = defaultdict(list), None

    for i in range(n):
        if i + 1 == p[i]:
            root = i + 1
        else:
            adjMap[p[i]].append(i + 1)
    
    
    res, stack = [], []
    visited = set()
    def findPaths(root, childrens):
        if not childrens:
            if root not in visited:
                stack.append(root)
                visited.add(root)
            res.append(stack.copy())
            stack.clear()
            return
        for child in childrens:
            if root not in visited:
               stack.append(root)
               visited.add(root)
            findPaths(child, adjMap[child]) 

    findPaths(root, adjMap[root] )  
    print(len(res))
    for path in res:
        print(len(path))
        print(*path)     

def main():
    testCases = int(input())
    for _ in range(testCases):
        runCases()

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
