class Solution:
    def compress(self, chars: List[str]) -> int:

        newLength = 0
        outerPtr = 0

        while outerPtr < len(chars):
            innerPtr = outerPtr
            while innerPtr < len(chars) and chars[innerPtr] == chars[outerPtr]:
                innerPtr += 1
            chars[newLength] = chars[outerPtr]
            newLength += 1

            if (innerPtr - outerPtr) > 1:
                groupLen = list(str(innerPtr - outerPtr))
                chars[newLength:newLength + len(groupLen)] = groupLen
                newLength += len(groupLen)

            outerPtr = innerPtr

        return newLength
