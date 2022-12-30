from functools import reduce
s = input().split(('+'))
s.sort()
print(reduce(lambda a,b: a + '+' + b, s))
