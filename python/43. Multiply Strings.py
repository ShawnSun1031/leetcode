class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for p1, m1 in enumerate(num1[::-1]):
            for p2, m2 in enumerate(num2[::-1]):
                ans += ((ord(m1)-ord("0"))*10**p1)*((ord(m2)-ord("0"))*10**p2)

        return str(ans)


if __name__ == "__main__":
    num1 = "123"
    num2 = "456"
    ans = "56088"
    # print(ord("1"))
    output = Solution().multiply(num1, num2)
    print(output)
