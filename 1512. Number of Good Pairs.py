class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count, hashMap = 0, {}
        for num in nums:
            if hashMap.get(num, 0):
                count += hashMap[num]
                hashMap[num] += 1
            else:
                hashMap[num] = hashMap.get(num, 0) + 1 
        return count
