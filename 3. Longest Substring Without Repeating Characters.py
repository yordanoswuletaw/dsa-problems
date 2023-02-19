class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashMap = {}
        longestLen = 0
        slow = fast = 0
        while fast < len(s):
            # updating length of the longest substring
            if s[fast] in hashMap:
                longestLen = max(longestLen, fast - slow)
                slow = max(slow, hashMap[s[fast]] + 1)
                hashMap.pop(s[fast])
            # storing unique characters
            else:
                hashMap[s[fast]] = fast 
                fast += 1

        longestLen = max(longestLen, fast - slow)
        return longestLen
        
