class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph, degree = defaultdict(list), defaultdict(int)

        for v, u in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        nums = []
        for key, val in degree.items():
            if val == 1:
                visited, curr = set(), key
                while curr not in visited:
                    nums.append(curr)
                    visited.add(curr)
                    for nxt in graph[curr]:
                        if nxt not in visited:
                            curr = nxt
                            break
                break
        
        return nums


       
