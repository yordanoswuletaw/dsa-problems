class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        queue = deque([("0000", 0)])
        visited = set(deadends)
        src = "0000"
        if src in visited:
            return - 1
        visited.add(src)

        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            for i in range(4):
                incLock = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:]
                if incLock not in visited:
                    queue.append((incLock, turns + 1))
                    visited.add(incLock)
                decLock = lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i + 1:]
                if decLock not in visited:
                    queue.append((decLock, turns + 1))
                    visited.add(decLock)
                 
        return -1
