# Enter your code here. Read input from STDIN. Print output to STDOUT
def checkStricktSuperSet():
    setA = input().split(' ')
    n = int(input())
    for i in range(n):
        setB = input().split(' ')
        for each in setB:
            if each not in setA:
                return False 
    return True
            
print(checkStricktSuperSet())
