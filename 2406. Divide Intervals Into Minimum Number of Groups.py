class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        hashMap = defaultdict(int)

        for s, e in intervals:
            hashMap[s] += 1
            hashMap[e + 1] -= 1
        
        acc = groupNum = 0

        for val in sorted(hashMap.keys()):
            acc += hashMap[val]
            groupNum = max(acc, groupNum)
        
        return groupNum
