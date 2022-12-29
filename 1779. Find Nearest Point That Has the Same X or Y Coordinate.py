class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        nPoint, maxDistance = -1, float('inf')
        for i,point in enumerate(points):
            if point[0] == x or point[1] == y:
                dist = abs(x - point[0]) + abs(y - point[1])
                if dist < maxDistance:
                    nPoint, maxDistance = i, dist
        return nPoint
