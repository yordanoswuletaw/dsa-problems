class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        # merge the source codes with \n special charater to iterate over easily
        source = '\n'.join(source)
        output, i = '', 0
        
        while i < len(source):
            # remove blok comment
            if i < len(source) - 1 and source[i: i+2] == '/*':
                j = i + 2
                while j < len(source) - 2 and not source[j:j+2] == '*/':
                    j += 1
                i = j + 2
            
            # remove line comment
            elif i < len(source) - 1 and source[i: i+2] == '//':
                j = i + 1
                while j < len(source) and not source[j] == '\n':
                    j += 1
                i = j

            else:
                output += source[i]
                i += 1
    
        return [each for each in output.split('\n') if each != '']
