import sys
from collections import defaultdict
def main():
    n = int(sys.stdin.readline())
    adjMat = []
    for _ in range(n):
        adjMat.append(list(map(int, sys.stdin.readline().split())))
    
    source  = []
    sink  = []

    for i in range(n):
        isSource = True
        for j in range(n):
            if i != j and adjMat[j][i] != 0:
                isSource =False 
                break
        if isSource:
            source.append(i + 1) 
    
    for i in range(n):
        isSink = True 
        for j in range(n):
            if i != j and adjMat[i][j] != 0:
                isSink = False
                break
        if isSink:
            sink.append(i + 1) 
    
    print(len(source), *source)
    print(len(sink), *sink)

if __name__ == '__main__':
    main()
