class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()
        left, right = 0, min(n - 1, m - 1)

        def is_possible(k, pills, strength):
            ws = SortedList(workers[m-k-1:])
            for i in range(k, -1, -1):
                if ws[-1]  >= tasks[i]:
                    ws.pop()
                else:
                    if pills == 0:
                        return False
                    worker_indx = ws.bisect_left(tasks[i] -  strength)
                    if worker_indx == len(ws):
                        return False
                    pills -= 1
                    ws.pop(worker_indx)
            
            return True

        while left <= right:
            k = left + (right - left) // 2
            if is_possible(k, pills, strength):
                left = k + 1
            else:
                right = k - 1
        
        return left
        