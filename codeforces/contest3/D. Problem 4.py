from collections import OrderedDict
word = input()


wordMap = OrderedDict()
hello = ['o','l','l','e','h']
for char in word:
    if char == hello[-1]:
        hello.pop()
    if not hello:
        break

print('NO') if hello else print('YES')
        
