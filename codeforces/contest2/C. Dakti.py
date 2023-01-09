n = int(input())
'''
Approach: HashMap
'''
for _ in range(n):
    words = input().split()
    wordMap = {}
    for w in words:
        nums, i = '', 0
        word = w

        # remove digits from the word and storing the remaing words in dictionary using the removed digit as a key
        while i < len(word):
            if ord(word[i]) >= 48 and ord(word[i]) <= 57:
                nums += word[i]
                word = word[:i] + word[i+1:] 
            else:
                i += 1
        wordMap[int(nums)] = word 

    print(' '.join(dict(sorted(wordMap.items())).values()))

