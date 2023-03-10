class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        for dir in path.split("/"):
            # if there is no path and path is in the current directory
            if dir == "" or dir == ".":
                pass
            # if path is one up a level
            elif dir == "..":
                if stack:
                   stack.pop()
            else:
                stack.append(dir)
        
        return '/' + '/'.join(stack)

      
