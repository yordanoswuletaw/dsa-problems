class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        hashMap = defaultdict(int)

        for bill in bills:
            if bill == 5:
                hashMap[bill] += 1
            elif bill == 10:
                if hashMap[5] <= 0:
                    return False
                hashMap[bill] += 1
                hashMap[5] -= 1
            else:
                if hashMap[5] > 0 and hashMap[10] > 0:
                    hashMap[5] -= 1
                    hashMap[10] -= 1
                elif hashMap[5] >= 3:
                    hashMap[5] -= 3
                else:
                    return False
        
        return True
