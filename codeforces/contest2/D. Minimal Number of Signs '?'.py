'''
Intuition: Matrix, Greedy
Complexity: 
   Time Complexity: O(n * m)
   Space COmplexity: O(1)
'''

n = int(input())
output = []
    
for _ in range(n):
        pattern = input()
        # if we have more than one pattern
        if output:
            for i in range(len(pattern)):
                # check if pattern match ??? or aaa
                if output[i] == pattern[i]:
                    continue
                # check if pattern match *a or *?
                elif output[i] == '*':
                    if pattern[i] == '?':
                        continue
                    else:
                        output[i] = pattern[i]
                # check if pattern match ?
                elif output[i] == '?':
                     continue
                # check if the current pattern is different from the comulative pattern
                elif output[i] != pattern[i] != '?':
                    output[i] = '?'          
        else:
            for i in range(len(pattern)):
                # * is special character which replaced later for pattern optimization
                if pattern[i] == '?':
                    output.append('*')
                else:
                    output.append(pattern[i])
        

print(''.join(map(lambda char: 'y' if char == '*' else char, output)))


