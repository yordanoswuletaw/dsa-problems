class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        totalSeats = [0] * (n + 1)

        for each in bookings:
            totalSeats[each[0] - 1] += each[2]
            totalSeats[each[1]] -= each[2]
        
        for i in range(1, n):
            totalSeats[i] += totalSeats[i - 1]
        
        return totalSeats[:-1]
