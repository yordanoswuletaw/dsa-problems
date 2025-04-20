class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        freqs = Counter(answers)
        tot_min_rabbits = 0
        for color, freq in freqs.items():
            if freq > color:
                tot_min_rabbits += (color + 1) * (freq // (color + 1))
                freq = freq % (color + 1)
            if freq >= 1:
                tot_min_rabbits += 1 + color
        
        return tot_min_rabbits
            
            
        