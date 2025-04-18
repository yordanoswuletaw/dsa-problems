class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        seq = [1] 
        for i in range(n - 1):
            temp_seq = []
            j = 0
            while j < len(seq):
                k = j + 1
                while k < len(seq) and seq[k] == seq[j]:
                    k += 1
                temp_seq.extend([str(k - j), str(seq[j])])
                j = k
            seq = temp_seq
        
        return ''.join(seq)