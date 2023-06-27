class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        hashMap = Counter(nums)
        while hashMap:
            seqCount = 0
            keys = list(hashMap.keys())
            prev = None
            for i, key in enumerate(keys):
                if i == 0:
                    hashMap[key] -= 1
                    seqCount += 1
                    prev = key
                else:
                    if hashMap[prev] < hashMap[key] and key - prev == 1:
                        hashMap[key] -= 1
                        seqCount += 1
                        prev = key
                    else:
                        break
                if hashMap[key] == 0:
                    hashMap.pop(key)
            if seqCount < 3:
                return False 

        return len(hashMap) == 0
                
