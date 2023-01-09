class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        output = []
        evenSum = sum(filter(lambda num: num % 2 == 0, nums))
        for i, query in enumerate(queries):
            if  nums[query[1]] % 2 == 0:
                nums[query[1]] += query[0]
                if  nums[query[1]] % 2 == 0:
                    evenSum += query[0]
                    output.append(evenSum)
                else:
                    evenSum -= (nums[query[1]] - query[0])
                    output.append(evenSum)
            else:
                nums[query[1]] += query[0]
                if nums[query[1]] % 2 == 0:
                    evenSum += nums[query[1]]
                    output.append(evenSum)
                else:
                    output.append(evenSum)

        return output
