class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        quotient = num // 3
        reminder = num % 3
        if reminder:
            return []
        else:
             return [quotient-1, quotient, quotient + 1] 
