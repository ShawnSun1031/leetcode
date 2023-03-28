# class Solution:
#     def runningSum(self, nums):
#         ans = [nums[0]]
#         for i in range(1, len(nums)):
#             ans.append(nums[i]+ans[-1])

#         return ans
# time : O(n^2)
# space : O(n)


class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
# time : O(n)
# space : O(n)


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    ans = [1, 3, 6, 10]
    output = Solution().runningSum(nums)
    print(output)
