class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        n, stack = len(arr), []

        for i in range(n - 1, -1, -1):
            if not stack or arr[stack[-1]] >= arr[i]:
                while stack and arr[stack[-1]] == arr[i]:
                    stack.pop()
                stack.append(i)
            else:
                break
        
        if stack and stack[-1] > 0:
            minIndx = stack[-1]
            maxIndx = minIndx - 1
            while stack and arr[maxIndx] > arr[stack[-1]]:
                minIndx = stack.pop()
            
            arr[maxIndx], arr[minIndx] = arr[minIndx], arr[maxIndx]
        
        return arr
