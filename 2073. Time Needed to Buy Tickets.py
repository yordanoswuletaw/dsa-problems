class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        round = tickets[k]
        timeTaken = 0
   
        for i,ticket in enumerate(tickets):
            if i > k:
                timeTaken += min(round - 1, ticket)
            else:
                timeTaken += min(round, ticket)
        
        return timeTaken
