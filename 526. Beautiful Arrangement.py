class Solution:
    def countArrangement(self, n: int) -> int:

        self.res = 0

        def backtrack(indx, arr):
            if indx >= n + 1:
                self.res += 1
                return

            for i in range(1, n + 1):
                if i not in arr and (indx % i == 0 or i % indx == 0):
                    arr.add(i)
                    backtrack(indx + 1, arr)
                    arr.remove(i)

        backtrack(1, set())
        return self.res
        

            
            
