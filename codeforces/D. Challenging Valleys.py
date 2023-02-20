n = int(input())

for _ in range(n):
    numsLen = int(input())
    nums = list(map(int, input().split()))
    i, j = 0, numsLen - 1

    while i <= j:
        if i < j and nums[i] >= nums[i+1]:
            i += 1
        if j > i and nums[j] >= nums[j-1]:
            j -= 1
        if i < j and nums[i] < nums[i + 1] and j > i and nums[j] < nums[j-1]:
            print('NO')
            break
        if i == j:
            print('YES')
            break
