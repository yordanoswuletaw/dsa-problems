class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = []
        self.times = times
        hashMap = defaultdict(int)
        currMax = None
        # rearinging the votes based on its query and time cast
        for person in persons:
            hashMap[person] += 1
            if currMax is None or hashMap[person] >= hashMap[currMax]: 
                self.persons.append(person)
                currMax = person
            else:
                self.persons.append(currMax)


    def q(self, t: int) -> int:
        leadingIndx = 0
        low, heigh = 0, len(self.times) - 1
        while low <= heigh:
            mid = low + (heigh - low) // 2
            # check if it is the most recent vote for time t
            if self.times[mid] <= t:
                leadingIndx = max(leadingIndx, mid)
                low = mid + 1
            else:
                heigh = mid - 1

        return self.persons[leadingIndx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
