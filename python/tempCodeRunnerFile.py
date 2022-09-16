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