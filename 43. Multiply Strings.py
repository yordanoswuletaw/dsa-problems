class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        products = []
        for i in range(len(num1)-1,-1,-1):
            currProduct, rem = '', 0
            for j in range(len(num2)-1, -1, -1):
                prod = int(num2[j]) * int(num1[i]) + rem
                currProduct =  currProduct + str(prod%10)
                rem = prod // 10
            if rem:
                currProduct = currProduct + str(rem) 
            currProduct = ('0' * (len(num1) - 1 - i)) + currProduct
            products.append(currProduct)
        print(products)

        maxLen = len(max(products, key=len))
        res, rem = '', 0
        for i in range(maxLen):
            currSum = 0
            for j in range(len(products)):
                if i < len(products[j]):
                    currSum += int(products[j][i])
            res += str((currSum + rem)% 10)
            rem = (currSum + rem) // 10
        if rem:
            res =  res + str(rem)
        i = len(res) - 1
        while i >= 1 and res[i] == '0':
            res = res[:i]
            i -= 1

        return res[::-1]
