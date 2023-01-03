class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        hashMap = {}
        for domain in cpdomains:
            # split the time and domain 
            time, currDomain = domain.split()
            # split each domain section
            currDomain = currDomain.split(".")
            time = int(time)

            for i in range(len(currDomain)):
                # sum up each domains visited time using hash map
                hashMap['.'.join(currDomain[i:])] = hashMap.get('.'.join(currDomain[i:]), 0) + time

        return [str(value) + ' ' + key for key, value in hashMap.items()]
