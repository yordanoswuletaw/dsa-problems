class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        '''
        Sort the array in a manner of the total skill of each team is equal
        '''
        skill.sort()
        # each players skill sum
        skillSum = skill[0] + skill[-1]
        # sum of the chemistry of all the teams
        chemistrySum = skill[0] * skill[-1]
        leftPtr, rightPtr = 1, len(skill) - 2

        while leftPtr < rightPtr:
            currSum = skill[leftPtr] + skill[rightPtr]
            # check if total skill of each teamis equal
            if skillSum != currSum:
                return -1
            chemistrySum += skill[leftPtr] * skill[rightPtr]
            leftPtr += 1
            rightPtr -= 1
        return chemistrySum
