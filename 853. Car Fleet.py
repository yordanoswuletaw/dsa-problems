class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        inp = [(p, s) for p, s in zip(position, speed)]
        inp.sort(reverse=True)
        print(inp)

        stack = []
        for each in inp:
            # calculating the time it takes to reach the target
            time = (target - each[0]) /  each[1]
            # checking if it can create a car fleet
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)
