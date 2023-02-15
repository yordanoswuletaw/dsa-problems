n = int(input())

segs = []
for _ in range(n):
    segs.append(tuple(map(int, input().split())))

dict = {}
for i, seg in enumerate(segs):
    dict[seg] = i + 1


def findSegment(dict, ssegs, n):
    start = ssegs[0][0]
    end = ssegs[0][1]
    indx = dict[ssegs[0]]
    for i in range(1, n):
        if ssegs[i][0] == start:
            if end < ssegs[i][1]:
                end = ssegs[i][1]
                indx = dict[ssegs[i]]
        elif ssegs[i][1] > end:
            return -1
    return indx 

print(findSegment(dict, sorted(segs, key=lambda seg: seg[0]), n))
