# Enter your code here. Read input from STDIN. Print output to STDOUT
def wordOrder():
    n = int(input())
    hashMap = {}
    for i in range(n):
        word = input()
        hashMap[word] = hashMap.get(word, 0) + 1
    print(len(hashMap))
    print(' '.join([str(i) for i in hashMap.values()]))
    
wordOrder()
