class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_table = defaultdict(list)
        for word in strs:
            hash_table[tuple(sorted(word))].append(word)
        
        return list(hash_table.values())
