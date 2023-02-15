n = int(input())

nums = sorted(map(int, input().split()))

i, j = 1, len(nums) - 1
if j % 2:
    j -= 1
while i <= j:
    nums[i], nums[j] = nums[j], nums[i]
    i += 2
    j -= 2
print(*nums)

