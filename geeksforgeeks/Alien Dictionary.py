#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        # creating adj matrix based on characters indexing order
        for i in range(1, N):
            prev, nxt = alien_dict[i - 1], alien_dict[i]
            m = len(prev)
            
            for i in range(m):
                if prev[i] != nxt[i]:
                    graph[prev[i]].append(nxt[i])
                    indegree[nxt[i]] += 1
                    indegree[prev[i]] += 0
                    break
        
        # applying topological sort   
        order = []
        queue = deque()
        for key, val in indegree.items():
            if val == 0:
                queue.append(key)
        
        while queue:
            char = queue.popleft()
            order.append(char)
            for nxt in graph[char]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
                    
        
        for word in alien_dict:
            for char in word:
                if char not in indegree:
                    order.append(char)
                    indegree[char] = 0
                    
        
        return ''.join(order)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
