res, n = 0, int(input())
for i in range(n):
    res += sum(map(int, input().split()))
print('YES') if res == 0 else print('NO')
