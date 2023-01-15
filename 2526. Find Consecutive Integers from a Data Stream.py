from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        # to track a number which equals to self.vaue
        self.eqValue = 0
        # to track a number which is not equal to value
        # self.notValue = -1    

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.eqValue += 1
        else:
            self.eqValue = 0
        return self.eqValue >= self.k

        # using Queue Ds
        # deque the queue if it is full
        # if len(self.queue) == self.k:
        #     self.queue.popleft() 
        #     self.notValue -= 1
        # self.queue.append(num)
        # # if we added not value number in the queue rare we reset self.notValue to k again
        # if num != self.value:
        #     self.notValue = len(self.queue) - 1
        # if len(self.queue) < self.k or self.notValue >= 0:
        #     return False 
        # return True 


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
