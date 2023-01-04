testcaseSize = int(input())

def checkReplacement(inputSize, letters, numbers):
    hashMap = {}

    for i in range(inputSize):
        if numbers[i] in hashMap:
            if hashMap[numbers[i]] != letters[i]:
                return 'NO' 
        else:
            hashMap[numbers[i]] = letters[i]
    return 'YES'

for _ in range(testcaseSize):
    inputSize = int(input())
    numbers = list(map(int, input().split()))
    letters = input()
    print(checkReplacement(inputSize, letters, numbers))

    
