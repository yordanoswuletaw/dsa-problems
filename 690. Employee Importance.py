"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adjList = defaultdict(lambda: 'Employee')
        for employee in employees:
            adjList[employee.id] = employee

        visited = set()

        def dfs(employee):
            if employee.id in visited:
                return 0
            visited.add(employee.id)
            importance = employee.importance
            for id in employee.subordinates:
                importance += dfs(adjList[id])
            return importance

        return dfs(adjList[id])
