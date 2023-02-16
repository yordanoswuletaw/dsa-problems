n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

merged = []

ptr1 = ptr2 = 0
while ptr1 < n and ptr2 < m:
    if arr1[ptr1] <= arr2[ptr2]:
        merged.append(arr1[ptr1])
        ptr1 += 1
    else:
        merged.append(arr2[ptr2])
        ptr2 += 1

if ptr1 < n:
    merged.extend(arr1[ptr1:])
elif ptr2 < m:
    merged.extend(arr2[ptr2:])

print(*merged)
