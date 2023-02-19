class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        counts = defaultdict(int)
        l, total, res = 0, 0, 0

        for r in range(len(fruits)):

            counts[fruits[r]] += 1
            total += 1

            while len(counts) > 2:
                counts[fruits[l]] -= 1
                total -= 1
                if not counts[fruits[l]]:
                    counts.pop(fruits[l])
                l += 1 
            res = max(res, total)
        return res
