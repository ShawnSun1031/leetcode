class Solution:
    def generateParenthesis(self, n: int):
        self.ans = []

        def backtracking(ans, left, right, stop, s):
            if len(s) == 2*stop:
                return ans.append(s)
            if left < stop:
                backtracking(ans, left+1, right, stop, s+"(")
            if right < left:
                backtracking(ans, left, right+1, stop, s+")")

        backtracking(self.ans, 0, 0, n, "")

        return self.ans


if __name__ == "__main__":
    n = 3
    ans = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    output = Solution().generateParenthesis(n)
    print(output)
