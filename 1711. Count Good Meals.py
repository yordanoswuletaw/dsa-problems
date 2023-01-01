class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:

        hashMap, goodMeals = {}, 0
        for i in deliciousness:
            for j in range(22):
                goodMeals += hashMap.get(2 ** j - i, 0)
            hashMap[i] = hashMap.get(i, 0) + 1
        return goodMeals % (10 ** 9 + 7)
    
        # bruit force
        # goodMeals = 0
        # for i in range(len(deliciousness) - 1):
        #     for j in range(i + 1, len(deliciousness)):
        #         if 0  ==  (log((deliciousness[i] + deliciousness[j]), 2)) * 10 % 10:
        #             goodMeals += 1
        # return goodMeals

