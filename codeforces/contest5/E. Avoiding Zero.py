def check(nums, l):
    ptvSum = sum(nums)
    ntvSum = sum(nums[::-1])
    if ptvSum < 0:
        print('YES')
        print(' '.join(map(str, nums)))
    elif ntvSum > 0:
        print('YES')
        print(' '.join(map(str, nums[::-1])))
    else:
        print('NO')
n = int(input())
for _ in range(n):
    l = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    check(nums, l)
