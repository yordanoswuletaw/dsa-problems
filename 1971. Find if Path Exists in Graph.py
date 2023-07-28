class UnionFind:

    def __init__(self, n: int):
        self.root = {i: i for i in range(n)}
        self.size = [1] * n
    
    def find(self, node1: int):
        if node1 == self.root[node1]:
            return node1
        self.root[node1] = self.find(self.root[node1])
        return self.root[node1]
    
    def union(self, node1: int, node2: int):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if self.size[root2] > self.size[root1]:
            self.root[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.root[root2] = root1
            self.size[root1] += self.size[root2]
    
    def connected(self, node1: int, node2: int):
        return self.find(node1) == self.find(node2)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # union find
        djSet = UnionFind(n)
        for x, y in edges:
            djSet.union(x, y)
        
        return djSet.connected(source, destination)

        # graph = defaultdict(list)
        # visited = set([source])
        # for edge in edges:
        #     graph[edge[0]].append(edge[1])
        #     graph[edge[1]].append(edge[0])
        
        # # bfs
        # queue = deque([source])
        # while queue:
        #     v = queue.popleft()
        #     if v == destination:
        #         return True 
        #     for neib in graph[v]:
        #         if neib not in visited:
        #             queue.append(neib)
        #             visited.add(neib)

        # return False 


        # # dfs iterative approach
        # stack = [source]
        # while stack:
        #     top = stack.pop()
        #     if top == destination:
        #         return True 
        #     for each in graph[top]:
        #         if each not in visited:
        #             stack.append(each)
        #             visited.add(each)
        
        # return False 

        # # dfsrecursive approach
        # def dfs(vertix, visited):
        #     if vertix in visited:
        #         return
        #     if vertix == destination:
        #         return True
            
        #     visited.add(vertix)
        #     for each in graph[vertix]:
        #         if dfs(each, visited):
        #             return True 
        
        # return dfs(source, set())
        
