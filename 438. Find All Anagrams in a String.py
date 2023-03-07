class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n, m = len(s), len(p)
        if n < m:
            return []

        substr = Counter(p)
        # creating first windows size
        window = Counter(s[:m])
        # check if the first window maches the sub string
        output = [0] if window == substr else []

        for i in range(m, n):
            # removing the previous element
            if window[s[i-m]] > 1:
                window[s[i - m]] -= 1
            else:
                window.pop(s[i - m])
            # adding the next element
            window[s[i]] += 1
            # checking if window maches the sub string 
            if window == substr:
                output.append(i - m + 1)
        
        return output
