class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        len1, len2 = len(players), len(trainers)
        ptr1= ptr2 = 0
        maxMachings = 0

        while ptr1 < len1 and ptr2 < len2:
            if players[ptr1] <= trainers[ptr2]:
                maxMachings += 1
                ptr1 += 1
                ptr2 += 1
            else:
                ptr1 += 1

        
        return maxMachings
