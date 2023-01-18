class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        wordDict = [0] * 26
        for char in words[0]:
            wordDict[ord(char) - 97] += 1
        for word in words[1:]:
            tempWordDict = [0] * 26
            for char in word:
                tempWordDict[ord(char) - 97] += 1
            for i in range(26):
                wordDict[i] = min(wordDict[i], tempWordDict[i])
        
        output = []
        print(wordDict)
        for key in range(26):
           output.extend([chr(97+key) for _ in range(wordDict[key])])
        return output

        # wordList = []
        # for word in words:
        #     hashMap = {}
        #     for ltr in word:
        #         hashMap[ltr] = hashMap.get(ltr, 0) + 1
        #     wordList.append(hashMap)
        
        # output = []
        # for ltr in tuple(set(words[0])):
        #     minVal = float('inf')
        #     for hashMap in wordList:
        #         minVal = min(minVal, hashMap.get(ltr, 0))
        #     if minVal:
        #         l = [ltr] * minVal
        #         output.extend(l)

        # return output
