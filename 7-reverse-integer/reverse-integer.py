class Solution:
    def reverse(self, x: int) -> int:

        min_range, max_range = -(2 ** 31), 2 ** 31 - 1
        reverse_x = 0
        prev_x = None
        while x and prev_x != x:
            if x >= 0:
                rem = x % 10
                if max_range - reverse_x * 10 < rem:
                    return 0
                reverse_x = reverse_x * 10 + rem
            else:
                rem = abs(x - int(x / 10) * 10)
                if min_range - reverse_x * 10 > -rem:
                    return 0
                reverse_x = reverse_x * 10 - rem
            prev_x = x
            x = int(x / 10)
        
        return reverse_x
