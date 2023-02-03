n = int(input())
y = list(map(int, input().split()))

has2parities = [False] * 2
for i in range(n):
    has2parities[y[i] % 2] = True 
if all(has2parities):
    print(*sorted(y))
else:
    print(*y)
