class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:


        arr = [-1] * (max(max(matches, key=lambda item: max(item))) + 1)
        for m in matches:
            if arr[m[0]] == -1:
                arr[m[0]] = 0
            if arr[m[1]] == -1:
                arr[m[1]] = 1
            else:
                arr[m[1]] += 1
        
        answer = [[], []]
        for i in range(len(arr)):
            if arr[i] == 0:
                answer[0].append(i)
            elif arr[i] == 1:
                answer[1].append(i)
     
        # using hashmap
        # hashMap = {}
        # for m in matches:
        #     if m[0] not in hashMap:
        #         hashMap[m[0]] = 0
        #     hashMap[m[1]] = hashMap.get(m[1], 0) + 1
        # answer = [[], []]
        # for key,val in hashMap.items():
        #     if val == 0:
        #         answer[0].append(key)
        #     elif val == 1:
        #         answer[1].append(key)
        # answer[0].sort()
        # answer[1].sort()
        
        return answer
        
