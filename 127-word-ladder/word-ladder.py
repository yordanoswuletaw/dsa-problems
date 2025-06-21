class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        n = len(wordList)
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        queue = deque([beginWord])
        visited = set([beginWord])
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                prev_word = queue.popleft()
                if prev_word == endWord:
                    return step
                for i in range(len(prev_word)):
                    for j in range(26):
                        char = chr(ord('a') + j)
                        word = prev_word[:i] + char + prev_word[i+1:]
                        if word in wordList and word not in visited:
                            queue.append(word)
                            visited.add(word)
        
        return 0