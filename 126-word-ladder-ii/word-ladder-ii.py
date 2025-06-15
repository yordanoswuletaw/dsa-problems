class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        # Building the graph
        n = len(wordList)
        graph = defaultdict(list)
        for word in [beginWord] + wordList:
            for nb in wordList:
                diff = 0
                for i in range(len(word)):
                    if word[i] != nb[i]:
                        diff += 1
                if diff == 1:
                    graph[word].append(nb)
        
        # Tracking the shortest path 
        queue = deque([beginWord])
        visited = set()
        hash_table = defaultdict(set)
        step = 0
        while queue:
            end_word_found = False
            for _ in range(len(queue)):
                word = queue.popleft()
                if word in visited:
                    continue
                visited.add(word)
                if word == endWord:
                    end_word_found = True
                for nb in graph[word]:
                    if nb not in visited:
                        hash_table[nb].add(word)
                        queue.append(nb)
                    if nb == endWord:
                        end_word_found = True
            step += 1
            if end_word_found:
                break

        # Identifying the shortest path
        if endWord not in hash_table:
            return []

        transformations = []
        def dfs(word, seq, step):
            if step < 0:
                return 
            if word == beginWord:
                transformations.append(seq.copy()[::-1])
                return
            
            for nxt in hash_table[word]:
                seq.append(nxt)
                dfs(nxt, seq, step - 1)
                seq.pop()

        dfs(endWord, [endWord], step)

        return transformations
        