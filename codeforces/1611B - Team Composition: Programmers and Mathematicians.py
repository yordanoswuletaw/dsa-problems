for _ in range(int(input())):
   
    p, m = map(int, input().split())
    print(min(min(p, m), (p + m) // 4)) 
