# class Solution:
#     def isHappy(self, n: int):
#         mydict = {}

#         def replaceSquare(n):
#             ans = 0
#             newn = n
#             power = 0
#             while newn >= 10:
#                 newn /= 10
#                 power += 1
#                 if int(newn) < 10:
#                     temp = int(newn)
#                     ans += temp**2
#                     # print(f'int newn : {newn}')
#                     newn = n - temp*10**power
#                     # print(f'minus : {newn}')
#                     n = n - temp*10**power
#                     # print(f'n : {n}')
#                     power = 0
#             ans += int(newn)*int(newn)
#             # print(f'last newn : {newn}')

#             return ans

#         while replaceSquare(n) not in mydict:
#             mydict[replaceSquare(n)] = True
#             print(mydict)
#             if replaceSquare(n) == 1:
#                 return True
#             n = replaceSquare(n)

#         return False

class Solution:
    def isHappy(self, n: int):
        myset = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])

            if n in myset:
                return False
            else:
                myset.add(n)

        return True


if __name__ == "__main__":
    n = 19
    ans = False
    output = Solution().isHappy(n)
    print(output)
