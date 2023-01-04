# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())

a = defaultdict(list)

for i in range(n):
    val = input()
    a[val].append(str(i + 1))
    
for j in range(m):
    val = input()
    if a[val]:
        print(' '.join(a[val]))
    else:
        print(-1)
    
