querylen = int(input())
queries = []
for _ in range(querylen):
    queries.append(input())

for query in queries:
    if len(set(query)) == 1:
        print(-1)
    else:
        print(''.join(sorted(query)))
