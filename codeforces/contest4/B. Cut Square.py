def checkSquare(a1, b1, a2, b2):
    for (w1, l1) in ((a1, b1), (b1, a1)):

        for (w2, l2) in ((a2, b2), (b2, a2)):
            if w1 == w2 == l1 + l2:
                return 'YES'
    return 'NO'
   
for _ in range(int(input())):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    print(checkSquare(a1, b1, a2, b2))

