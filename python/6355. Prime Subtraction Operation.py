# The Sieve of Eratosthenes
import bisect


# class Solution:
#     def primeSubOperation(self, nums):
#         def getPrimes(nums):
#             primes = [True for _ in range(nums+1)]
#             primes[1] = primes[0] = False
#             for i in range(2, int((nums+1)**0.5), 1):
#                 for j in range(i**2, nums+1, i):
#                     primes[j] = False

#             return [i for i in range(len(primes)) if primes[i] == True]

#         primes = getPrimes(max(nums))
#         prev = 0
#         for num in nums:
#             idx = bisect.bisect_left(primes, num)
#             q = []
#             if idx == 0:  # no primes smaller than num
#                 p = 0
#                 if num <= prev:
#                     return False
#             else:
#                 p = primes[idx-1]
#             req = num-p

#             while p < num:
#                 if (num-p) > prev:
#                     req = num-p
#                     break
#                 idx -= 1

#                 p = primes[idx-1]
#                 if idx == 0:  # no primes smaller than num
#                     p = 0
#                     if num <= prev:
#                         return False

#             if req <= prev:
#                 if num > prev:
#                     prev = num
#                 else:
#                     return False
#             else:
#                 prev = req

#         return True

class Solution:
    def primeSubOperation(self, nums):
        def getPrimes(nums):
            primes = [True for _ in range(nums+1)]
            primes[0] = primes[1] = False
            for i in range(2, int((nums+1)**0.5), 1):
                for j in range(i**2, nums+1, i):
                    primes[j] = False

            return [i for i in range(len(primes)) if primes[i] == True]

        primes = getPrimes(max(nums))
        prev = nums[-1]
        flag = 0
        for num in nums[-2::-1]:
            if num < prev:
                prev = num
                continue
            flag = 1
            for p in primes:
                if p < num and (num-p < prev):
                    # print(f"num p : {num}, {p}")
                    prev = num-p
                    flag = 0
                    break

            if flag == 1:
                return False

        return flag == 0


if __name__ == "__main__":
    nums = [8, 19, 3, 4, 9]
    ans = True
    output = Solution().primeSubOperation(nums)
    print(output)
