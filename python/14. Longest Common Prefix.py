class Solution:
    def longestCommonPrefix(self, strs):
        compare = strs[0]
        ans = ""

        min_len = 201
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)

        for i in range(min_len):
            is_common = True
            for s in strs[1:]:
                if s[i] == compare[i]:
                    continue
                else:
                    is_common = False
                    break
            if is_common:
                ans += compare[i]
            else:
                break

        return ans


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    strs = sorted(strs)
    print(f"min : {strs}")
    ans = "fl"
    output = Solution().longestCommonPrefix(strs)
    print(output)
