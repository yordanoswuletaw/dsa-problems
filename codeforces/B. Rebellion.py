for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    ops = 0
    left, right = 0, n - 1
    while left < right:
        if nums[left] and not nums[right]:
            nums[right] = nums[left]
            left += 1
            right -= 1
            ops += 1
        elif not nums[left]:
            left += 1
        elif nums[right]:
            right -= 1
    
    print(ops)
        
