n = int(input())
'''
Approach: Greedy
'''
scores = list(map(int, input().split()))
res = 0
i = 0
min, max = scores[0], scores[0]
while i < len(scores):
        if max < scores[i]:
            res += 1
            max = scores[i]
        if min > scores[i]:
            res += 1
            min = scores[i]
        i += 1
print(res)
