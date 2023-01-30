def checkMove(stng, strengths):
    for s in strengths:
        if stng <= s[0]:
            return 'NO'
        stng += s[1]
    return 'YES'
stng, n  = map(int, input().split())
strengths = []
for _ in range(n):
    strengths.append(tuple(map(int, input().split())))
strengths.sort(key=lambda x: x[0])
print(checkMove(stng, strengths))
