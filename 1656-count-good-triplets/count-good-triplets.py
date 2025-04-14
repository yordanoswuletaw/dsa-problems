class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        counts = 0
        def condition(x, y, z):
            return abs(x - y) <= a and abs(x - z) <= c and abs(y - z) <= b

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if condition(arr[i], arr[j], arr[k]):
                        counts += 1
        
        return counts