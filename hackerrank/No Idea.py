# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
arr = list(map(int, input().split()))
A, B = set(map(int, input().split())), set(map(int, input().split()))
happiness = 0
for val in arr:
    if val in A:
        happiness += 1
    elif val in B:
        happiness -= 1
print(happiness)
