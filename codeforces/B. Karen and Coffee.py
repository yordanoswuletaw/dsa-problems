def main():
    n, k, q = map(int, input().split())
    recipes = []
    quries = []
    MAX_RANGE = 200002

    for i in range(n):
        recipes.append(tuple(map(int, input().split())))
    
    for i in range(q):
        quries.append(tuple(map(int, input().split())))
    
    # creating exclusive prefix sum of n + 2 to inbound first and last element
    prfxSum = [0] * MAX_RANGE
    for start, end in recipes:
        prfxSum[start] += 1
        prfxSum[(end + 1)] -= 1
    
    # prefixsum to check if the recipe is admissible
    for i in range(1, MAX_RANGE):
        prfxSum[i] += prfxSum[i - 1]
    
    # normalizing admissible recipes to 1 and others to 0
    for i in range(MAX_RANGE):
        if prfxSum[i] >= k:
            prfxSum[i] = 1
        else:
            prfxSum[i] = 0
    
    # running other prefixsum to get the range of admissible recipes 
    for i in range(1, MAX_RANGE):
        prfxSum[i] += prfxSum[i - 1]
    
    # print admissable recipes in a given range
    for start, end in quries:
        print(prfxSum[end] - prfxSum[start - 1])
    

if __name__ == '__main__':
    main()
 
