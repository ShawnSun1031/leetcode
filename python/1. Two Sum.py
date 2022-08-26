class Solution:
    def twoSum(self, nums, target: int):
         ans = {}
         for idx, i in enumerate(nums):
            if (target-i) not in ans:
                ans[i] = idx
            else:
                return [ans[target-i], idx]

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    s = Solution().twoSum(nums,target)
    print(s)
    