class Solution:
    def singleNumber(self, nums):
<<<<<<< HEAD
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
=======
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
>>>>>>> 0c910dec3975a9c431607bac7b66299960d2cd4a
