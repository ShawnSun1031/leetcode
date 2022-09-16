class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        window_idx = []
        head = 0
        tail = -1
        length = 0
        for idx, c in enumerate(s):
            if c not in window:
                window.append(c)
                window_idx.append(idx)
                tail = idx
            else:
                if window[-1] == c:
                    head = idx
                    tail = idx
                    window = [c]
                    window_idx = [idx]
                else:
                    find_head = window.index(c)
                    head = window_idx[find_head] + 1
                    tail = idx
                    window = window[find_head+1:] + [c]
                    window_idx = window_idx[find_head+1:] + [idx]
            if (tail-head+1) > length:
                length = tail - head + 1
        return length


""" python split on str faster than list --> O(n^2)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub_str = ''
        max_len = 0
        
        for w in s:
            while w in sub_str:
                sub_str = sub_str[1:]
            else:
                sub_str += w
                max_len = max(len(sub_str), max_len)
        
        return max_len
"""

""" optimal solution --> O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
                
            used[c] = i
        return max_length
"""

if __name__ == "__main__":
    s = "aabaab!bb"
    ans = Solution().lengthOfLongestSubstring(s)
    print(ans)
