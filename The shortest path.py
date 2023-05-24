from collections import defaultdict, deque

def main():
    n, m = map(int, input().split())
    src, dest = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    visited = {src: None}
    queue = deque([src])

    while queue:
        node = queue.popleft()
        if node == dest:
            break

        for neib in graph[node]:
            if neib not in visited:
                visited[neib] = node 
                queue.append(neib)
    
    if dest in visited:
        paths = deque()
        node = dest
        while node in visited:
            paths.appendleft(node)
            node = visited[node]
        print(len(paths) - 1)
        print(*paths)
    else:
        print(-1)


if __name__ == '__main__':
    main()
