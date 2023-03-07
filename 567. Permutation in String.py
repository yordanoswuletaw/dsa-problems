class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        perm = Counter(s1)
        window = Counter(s2[:n1])
        left = 0
        for i in range(n1, n2):
            if window == perm:
                return True
            # adding a new value to the window
            window[s2[i]] += 1

            # removing previous value
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                window.pop(s2[left])
                
            left += 1            

        return window == perm
