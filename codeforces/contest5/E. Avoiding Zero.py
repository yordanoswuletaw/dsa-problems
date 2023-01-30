n = int(input())
for _ in range(n):
    l = int(input())
    nums = list(map(int, input().split()))
    numsSum = sum(nums)
    if numsSum > 0:
         print('YES')
         print(*sorted(nums, reverse=True))
    elif numsSum < 0:
        print('YES')
        print(*sorted(nums))
    else:
        print('NO')
