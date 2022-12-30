n = int(input())
x,y,z = 0,0,0
for i in range(n):
    vector = tuple(map(int, input().split()))
    x, y, z = x + vector[0], y + vector[1], z + vector[2]
print('YES') if x == y ==z == 0 else print('NO')
