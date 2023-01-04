testCaseSize = int(input())

for _ in range(testCaseSize):
    tShirt1, tShirt2 = input().split()
    if tShirt1[-1] == tShirt2[-1] == 'S':
        if len(tShirt1) < len(tShirt2):
            print('>')
        elif len(tShirt1) == len(tShirt2):
            print('=')
        else:
            print('<')

    elif tShirt1[-1] == tShirt2[-1] == 'L':
        if len(tShirt1) > len(tShirt2):
            print('>')
        elif len(tShirt1) == len(tShirt2):
            print('=')
        else:
            print('<')

    elif tShirt1[-1] == 'L':
        print('>') 

    elif tShirt1[-1] == 'M':
        if tShirt2[-1] == 'M':
            print('=')
        elif tShirt2[-1] == 'L':
            print('<') 
        else:
            print('>')

    elif tShirt1[-1] == 'S':
        print('<') 
