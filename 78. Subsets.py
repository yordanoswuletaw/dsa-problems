class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        powerSet, n = [[]], len(nums)

        def dfs(indx, currSet):
            if indx >= n:
                return 
            
            for i in range(indx, n):
                # adding each consecutive value to our set 
                currSet.append(nums[i])
                powerSet.append(currSet.copy())
                dfs(i + 1, currSet)
                # removing already inserted values
                currSet.pop()

        dfs(0, []) 
        return powerSet
