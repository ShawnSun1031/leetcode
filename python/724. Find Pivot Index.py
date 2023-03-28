class Solution(object):
    def pivotIndex(self, nums):
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1


if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    ans = 3
    output = Solution().pivotIndex(nums)
    print(output)
