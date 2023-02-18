class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        n, i = len(s), 0
        output = []

        while i < n:
            # last index of character at index i
            lastIndx = s.rfind(s[i])

            indx = i + 1
            # updating last index 
            while indx < lastIndx:
                lastIndx = max(lastIndx, s.rfind(s[indx]))
                indx += 1
            lastIndx += 1
            output.append(lastIndx - i)
            i = lastIndx 
        
        return output
                
                


