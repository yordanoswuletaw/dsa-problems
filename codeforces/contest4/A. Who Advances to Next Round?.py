n, k = map(int, input().split())
scores = list(map(int, input().split()))
participantNumber = 0

while participantNumber < n and scores[participantNumber] >= scores[k-1] and scores[participantNumber] > 0:
    participantNumber += 1
print(participantNumber)
