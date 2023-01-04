from collections import Counter
testCaseSize = int(input())

for _ in range(testCaseSize):
    n, c = map(int, input().split())
    planets = Counter(input().split())
    minCost = 0
    for orbit, planet in planets.items():
        if planet >= c:
            minCost += c
        else:
            minCost += 1 * planet
    print(minCost)
