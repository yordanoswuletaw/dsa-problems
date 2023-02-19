for _ in range(int(input())):
    m = int(input())
    seq = list(map(int, input().split()))
    res = i = 0
    while i < m:
        curr = seq[i]
        j = i + 1
        if curr > 0:
            while j < m and seq[j] > 0:
                curr = max(curr, seq[j])
                j += 1 
        else:
            while j < m and seq[j] < 0:
                curr = max(curr, seq[j])
                j += 1 
        res += curr
        i = j
    print(res)
