class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        fofQ = [query.count(min(query)) for query in queries]
        fofW = sorted([word.count(min(word)) for word in words])
        
        answer = []

        for each in fofQ:
            minVal = 0
            low, heigh = 0, len(fofW) - 1
            # counting the number of words such that fofQ[i] < fofW
            while low <= heigh:
                mid = low + (heigh - low) // 2
                if each < fofW[mid]:
                    minVal = max(minVal, len(fofW) -  mid)
                    heigh = mid - 1
                else:
                    low = mid + 1
            answer.append(minVal)

        return answer

