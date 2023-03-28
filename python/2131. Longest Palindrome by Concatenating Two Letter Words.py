from collections import defaultdict


class Solution:
    def longestPalindrome(self, words):
        m = defaultdict(int)
        unpaired = ans = 0
        for w in words:
            if w[0] == w[1]:
                if m[w] > 0:
                    unpaired -= 1
                    m[w] -= 1
                    ans += 4
                else:
                    m[w] += 1
                    unpaired += 1
            else:
                if m[w[::-1]] > 0:  # w[::-1] -> reversed w
                    ans += 4
                    m[w[::-1]] -= 1
                else:
                    m[w] += 1
        if unpaired > 0:
            ans += 2
        return ans

# without hashmap


# class Solution:
#     def longestPalindrome(self, words):
#         counter, ans = [[0] * 26 for _ in range(26)], 0
#         for w in words:
#             a, b = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')
#             if counter[b][a]:
#                 ans += 4
#                 counter[b][a] -= 1
#             else:
#                 counter[a][b] += 1
#         for i in range(26):
#             if counter[i][i]:
#                 ans += 2
#                 break
#         return ans


if __name__ == "__main__":
    words = ["mm", "mm", "yb", "by", "bb", "bm", "ym", "mb", "yb", "by",
             "mb", "mb", "bb", "yb", "by", "bb", "yb", "my", "mb", "ym"]
    ans = 6
    output = Solution().longestPalindrome(words)
    print(output)

    # s = 'abcacba'
    # flag = True
    # for i, c in enumerate(s[-1::-1]):
    #     print(f's,c : {s[i]}, {c}')
    #     if s[i] != c:
    #         flag = False

    # print(flag)

    # ["mm", "mm", "yb", "by", "bb", "bm", "ym", "mb", "yb", "by",
    #     "mb", "mb", "bb", "yb", "by", "bb", "yb", "my", "mb", "ym"]

    # "mm": 2
    # "yb" "by" "yb" "by" "yb" "by" ("yb"
    # "bb": 3
    # "bm" "mb" "mb" "mb"
    # "ym" "my"

    # "dd" : 5
    # "aa" : 3
    # "bb" : 3
    # "cc" : 3
