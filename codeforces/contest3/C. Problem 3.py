n = int(input())
coins = sorted(map(int, input().split()), reverse=True)
leftSum = sum(coins)
rightSum = 0
i = 0
while leftSum >= rightSum:
    leftSum -= coins[i]
    rightSum += coins[i]
    i += 1
print(i)
