class Solution:
    def splitString(self, s: str) -> bool:

        self.result, n = False, len(s) 
        newS = s[:]

        def dfs(start, subs):
    
            if start >= n:
                # if the whole string s selected (that means we do not have two non empty substrings)
                if len(subs) <= 1:
                     return 
                found = True 
                for i in range(1, len(subs)):
                    print(subs[i - 1], subs[i])
                    if int(subs[i - 1]) -  int(subs[i]) != 1:
                        found = False 
                        break 
                if found:
                    self.result = True 
                return

            # this block of code splits string s 1 upto n - 1 pices with different combinations
            for i in range(start, n):
                subs.append(s[start: i + 1])
                dfs(i + 1, subs)
                subs.pop()
            
        dfs(0, [])
        return self.result


