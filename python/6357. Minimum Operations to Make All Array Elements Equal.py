# class Solution:
#     def minOperations(self, nums, queries):
#         ans = []
#         for q in queries:
#             temp = 0
#             for num in nums:
#                 temp += abs(q-num)
#             ans.append(temp)

#         return ans

class Solution:
    def minOperations(self, nums, queries):
        ans = [[] for _ in range(len(queries))]
        nums.sort()
        length = len(nums)
        prefix = [0]
        temp = 0
        for num in nums:
            temp += num
            prefix.append(temp)
        # print(prefix)

        def find_idx(a, x):
            lo, hi = 0, len(a)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if a[mid] > x:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        for idx, q in enumerate(queries):
            sum_idx = find_idx(nums, q)
            # print(sum_idx)
            # print(f"test sum : {(length-sum_idx)}")
            ans[idx] = q*(sum_idx) - 2*prefix[sum_idx] + \
                prefix[-1] - q*(length-(sum_idx))

        # print(f"prefix : {prefix}")
        return ans


if __name__ == "__main__":
    nums = [2, 9, 6, 3]  # [1,3,6,8]
    queries = [10]
    ans = [14, 10]
    output = Solution().minOperations(nums, queries)
    print(output)
