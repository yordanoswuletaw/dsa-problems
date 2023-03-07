class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        hashMap = defaultdict(int)
        left = right = 0
    
        while right < len(s):
            hashMap[s[right]] += 1
            right += 1
            if right - left - max(hashMap.values()) <=  k:
                l = max(l, right - left)
            else:
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0:
                    hashMap.pop(s[left])
                left += 1
        
        return l
