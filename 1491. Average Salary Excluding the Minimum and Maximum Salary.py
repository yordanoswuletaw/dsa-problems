class Solution:
    def average(self, salary: List[int]) -> float:

        minSal, maxSal, salSum = float('inf'), float('-inf'), 0
        for each in salary:
            salSum += each
            minSal, maxSal = min(minSal, each), max(maxSal, each)
        
        return (salSum - minSal - maxSal) / (len(salary) - 2)
