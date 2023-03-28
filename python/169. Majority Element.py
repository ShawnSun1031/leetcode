# space : O(n) time : O(n)
class Solution:
    def majorityElement(self, nums):
        mydict = {}
        for n in nums:
            mydict[n] = 0
        for n in nums:
            mydict[n] += 1
        for k in mydict.keys():
            if mydict[k] > len(nums)//2:
                return k

# space : O(1) time : O(n)
# Boyer–Moore majority vote algorithm


class Solution:
    def majorityElement(self, nums):
        count = 1
        major = nums[0]
        for n in nums[1:]:
            if n == major:
                count += 1
            elif count == 0:
                major = n
            else:
                count -= 1

        return major


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    ans = 2
    output = Solution().majorityElement(nums)
    print(output)
