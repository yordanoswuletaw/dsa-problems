from collections import Counter
n = int(input())
members = input().split()
bad_memebers, excellent_members = Counter(input().split()), 0
for member in members:
    if len(set(member)) == len(member) and not bad_memebers.get(member, False):
        excellent_members += 1
print(excellent_members)

