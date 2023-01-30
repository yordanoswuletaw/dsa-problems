def isNonDegenerate(sides, n):
    # index of each sides of a triangle
    i, j, k = 0, 1, 2
    while k < n:
        # check for non-degenerate triangle
        if sides[k] < sides[i] + sides[j]:
            return 'YES'
        i += 1
        j += 1
        k += 1
    return 'NO'

n = int(input())
sides = list(map(int, input().split()))
print(isNonDegenerate(sorted(sides), n))
