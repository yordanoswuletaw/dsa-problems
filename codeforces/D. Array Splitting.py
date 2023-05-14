def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    suffixSum = []
    totalSum = 0
    for i in range(n - 1, -1, -1):
        totalSum += nums[i]
        if i > 0:
            suffixSum.append(totalSum)
    
    suffixSum.sort(reverse=True)
    for i in range(k - 1):
        totalSum += suffixSum[i]
    
    print(totalSum)

if __name__ == '__main__':
    main()

