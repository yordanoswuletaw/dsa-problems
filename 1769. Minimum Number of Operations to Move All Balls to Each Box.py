class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        nonEmpty = {}
        for i, box in enumerate(boxes):
            if box == '1':
                nonEmpty[i] = i
        
        output = []
        for i in range(len(boxes)):
            res = 0
            for key, value in nonEmpty.items():
                res += abs(i - value)
            output.append(res)
        
        return output
