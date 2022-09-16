class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        for i in range(int(n/2)+1):
            ans += self.combination(n-i*2+i)/(self.combination(i)
                                              * self.combination(n-i*2))
        return int(ans)

    def combination(self, c):
        p = 1
        for i in range(1, c+1):
            p *= i
        return p


""" optimal solution --> DP solve
class Solution:
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
"""

if __name__ == "__main__":
    n = 2
    ans = Solution().climbStairs(n)
    print(ans)
