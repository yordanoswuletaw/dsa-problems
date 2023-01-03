class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        hashMap = {}

        for path in paths:
            # split the file and its directory
            files = path.split()
            directory = files[0]

            for i in range(1, len(files)):
                # split the filename and its content
                fileName, content = files[i].split('(')
                # store each file full path in a hash map using the file content as key
                if content in hashMap:
                    hashMap[content].append(directory + '/' + fileName)
                else:
                    hashMap[content] = [directory + '/' + fileName]

        return [value for value in hashMap.values() if len(value) > 1]
