class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int):
        if (numOnes+numZeros) >= k:
            if numOnes >= k:
                return k
            else:
                return numOnes
        else:
            return numOnes-(k-numOnes-numZeros)


if __name__ == "__main__":
    numOnes = 3
    numZeros = 2
    numNegOnes = 0
    k = 4
    ans = 3
    output = Solution().kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)
    print(output)
