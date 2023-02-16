n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count = []

ptr1 = 0
for each in arr2:
    while ptr1 < n and arr1[ptr1] < each:
        ptr1 += 1
    count.append(ptr1)

print(*count)
