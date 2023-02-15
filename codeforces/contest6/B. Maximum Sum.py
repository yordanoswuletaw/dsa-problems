n, m = map(int, input().split())

tvSets = sorted(map(int, input().split()))
maxSumMoney = 0
for i,tv in enumerate(tvSets):
    if tv >= 0 or i >= m:
        break 
    maxSumMoney += tv 
print(abs(maxSumMoney))
