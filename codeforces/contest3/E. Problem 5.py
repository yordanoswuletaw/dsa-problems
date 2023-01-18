n, length = map(int, input().split())
laterns = sorted(map(int, input().split()))

dist = 0
i, j = 0, 1
while j < n:
    dist = max(laterns[j] - laterns[i], dist)
    i += 1
    j += 1
dist = dist/2
dist = max(dist, laterns[0], length - laterns[-1])
print(dist)
