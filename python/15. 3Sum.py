class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                if (nums[l] + nums[r]) == -nums[i]:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif (nums[l]+nums[r]) > -nums[i]:
                    r -= 1
                elif (nums[l]+nums[r]) < -nums[i]:
                    l += 1

        return list(ans)


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    ans = [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3],
           [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
    output = Solution().threeSum(nums)
    print(output)
    # error = [[-4, 1, 3], [-3, -1, 4], [-3, 1, 2], [-1, -1, 2]]
