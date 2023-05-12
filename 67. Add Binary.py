class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res, rem = [], 0
        n, m = len(a), len(b)
        i = 0
        a = a[::-1]
        b = b[::-1]

        while i < min(n, m):
            if int(a[i]) and int(b[i]):
                res.append(str(rem))
                rem = 1
            elif int(a[i]) or int(b[i]):
                res.append(str(int(not rem)))
            else:
                res.append(str(rem))
                rem = 0
            i += 1
    
        if i < n:
            while i < n:
                if int(a[i]):
                    res.append(str(int(not rem)))
                else:
                    res.append(str(rem))
                    rem = 0
                i += 1
    
        if i < m:
            while i < m:
                if int(b[i]):
                    res.append(str(int(not rem)))
                else:
                    res.append(str(rem))
                    rem = 0
                i += 1
        
        if rem:
            res.append(str(rem))
        
        return ''.join(res[::-1])

                
