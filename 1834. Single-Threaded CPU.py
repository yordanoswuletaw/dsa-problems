class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        
        heap = [(tasks[0][1], tasks[0][2])]
        tasksOrder, indx, duration = [], 1, tasks[0][0]

        while heap:
            ptime, i = heappop(heap)
            duration += ptime
            tasksOrder.append(i)
            # executing tasks instantly
            while indx < len(tasks) and tasks[indx][0] <= duration:
                heappush(heap, (tasks[indx][1], tasks[indx][2]))
                indx += 1
            # allocating new task after cpu is idel 
            if not heap and indx < len(tasks):
                heappush(heap, (tasks[indx][1], tasks[indx][2]))
                duration = tasks[indx][0]
                indx += 1

        return tasksOrder
