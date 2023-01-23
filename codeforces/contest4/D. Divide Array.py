n = int(input())
nums = list(map(int, input().split()))

ntv = []
ptv = []
zeros = []

for num in nums:
    if num == 0:
        zeros.append(num)
    elif num > 0:
        ptv.append(num)
    else:
        ntv.append(num)
if ptv:
    if len(ntv) % 2 == 0:
        zeros.append(ntv.pop())
else:
    i = 0
    while ntv and i < 2:
        ptv.append(ntv.pop())
        i += 1
    if len(ntv) % 2 == 0:
        zeros = [ntv.pop()] + zeros

print(len(ntv), ' '.join([str(i) for i in ntv]))
print(len(ptv), ' '.join([str(i) for i in ptv]))
print(len(zeros), ' '.join([str(i) for i in zeros]))

    
