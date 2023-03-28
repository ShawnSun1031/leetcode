class Solution:
    def singleNumber(self, nums):
        mydict = {}
        for i in nums:
            mydict[i] = 0
        for i in nums:
            mydict[i] += 1
        for k in mydict.keys():
            if mydict[k] == 1:
                return k

        return 0


# bit manipulation
class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
            print(f'xor : {xor}')

        return xor


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    ans = 4
    output = Solution().singleNumber(nums)
    print(output)
