class Solution:
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        result = {}
        for n in nums:
            if n not in result:
                result[n] = n
            else:
                del result[n]
                
        return list(result.keys())[0]


if __name__ == "__main__":
    nums = [4,1,2,1,2]
    ans = Solution().singleNumber(nums)
    print(ans)