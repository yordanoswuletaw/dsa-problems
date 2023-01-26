class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        hashMap = defaultdict(int)
        for i, num in enumerate(sorted(nums, reverse=True)):
            if hashMap[num] :
                hashMap[num] -= 1
            else:
                hashMap[num] = len(nums) - i - 1
        
        output = []
        for num in nums:
            output.append(hashMap[num])
        
        return output
