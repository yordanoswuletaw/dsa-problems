from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		
		graph = defaultdict(list)
		colors = defaultdict(int)
		
		for i in range(len(adj)):
		    graph[i] = adj[i]
		
		def isCycle(node, prev, colors):
		    colors[node] = -1
		    for neib in graph[node]:
		        if colors[neib] == 1:
		            continue
		        elif colors[neib] == -1:
		            if prev == neib:
		                continue
		            else:
		                return True
		        else:
		            if isCycle(neib, node, colors):
		                return True
		    colors[node] = 1
		    
		
		for node in range(V):
		    if colors[node] == 0:
		        if isCycle(node, None, colors):
		            return 1
		
		return 0
		
		


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
