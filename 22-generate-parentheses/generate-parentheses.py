class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        all_generated = set()
        def generate(n, generated):
            if not n:
                all_generated.add(''.join(generated))
                return
            
            for i in range(1, len(generated) + 1):
                generate(n - 1, generated[:i] + ['(', ')'] + generated[i:])
        
        generate(n - 1, ['(', ')'])
        return list(all_generated)