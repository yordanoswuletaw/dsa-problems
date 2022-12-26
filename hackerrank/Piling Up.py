# Enter your code here. Read input from STDIN. Print output to STDOUT
def pilingUp():
    T = int(input())
    for i in range(T):
        size = int(input())
        block = list(map(int, input().split()))
        if size == 1:
            yield 'Yes'
        i, j = 0, size - 1
        while i <= j and i < size and j >= 0:
            
            if block[i] >=  block[i+1]:
                i += 1
            if block[j] >= block[j-1]:
                j -= 1
            if block[i] < block[i+1] and block[j] < block[j-1]:
                break
        yield 'Yes' if i >= j else 'No'
        
for i in pilingUp():
    print(i)
            
