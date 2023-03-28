class Solution:
    def generate(self, numRows: int):
        ans = [[] for i in range(numRows)]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        ans[0] = [1]
        ans[1] = [1, 1]
        for i in range(2, numRows):
            ans[i] = [1 for _ in range(i+1)]
            for j in range(1, len(ans[i])-1):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

        return ans


if __name__ == "__main__":
    numRows = 5
    ans = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    output = Solution().generate(numRows)
    print(output)
