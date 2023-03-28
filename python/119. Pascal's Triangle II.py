class Solution:
    def getRow(self, rowIndex: int):
        ans = [[1]]
        if rowIndex == 0:
            return [1]
        else:
            for _ in range(rowIndex):
                ans.append([a+b for a, b in zip(ans[-1]+[0], [0]+ans[-1])])

            return ans[rowIndex]


if __name__ == "__main__":
    rowIndex = 3
    ans = [1, 3, 3, 1]
    out = Solution().getRow(rowIndex)
    print(out)
