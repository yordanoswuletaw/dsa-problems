def check(array):
    i, j = 0, 1
    while j < len(array):
        if array[j] - array[i] > 1:
            return 'NO'
        j += 1
        i += 1
    return 'YES'
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    print(check(sorted(array)))
