# class Solution:
#     def findBall(self, grid):
#         # (1,1) : col+1 (-1,-1) : col-1
#         rows = len(grid)
#         cols = len(grid[0])
#         ans = []
#         for c in range(cols):
#             curr_c = c
#             for r in range(rows):
#                 if grid[r][curr_c] == 1:
#                     if curr_c+1 == cols:
#                         curr_c = -1
#                         break
#                     if grid[r][curr_c+1] == 1:
#                         curr_c += 1
#                     else:
#                         curr_c = -1
#                         break
#                 elif grid[r][curr_c] == -1:
#                     if curr_c-1 < 0:
#                         curr_c = -1
#                         break
#                     if grid[r][curr_c-1] == -1:
#                         curr_c -= 1
#                     else:
#                         curr_c = -1
#                         break

#                 if curr_c < 0:
#                     curr_c = -1
#                     break

#             ans.append(curr_c)

#         return ans


class Solution:
    def findBall(self, grid):
        m, n = len(grid), len(grid[0])

        def helper(r, c):
            if r == m:
                return c
            elif grid[r][c] == 1 and c+1 < n and grid[r][c+1] == 1:
                return helper(r+1, c+1)
            elif grid[r][c] == -1 and 0 <= c-1 and grid[r][c-1] == -1:
                return helper(r+1, c-1)
            else:
                return -1

        return [helper(0, j) for j in range(n)]

# DP solution
# class Solution:
#     def findBall(self, grid: List[List[int]]) -> List[int]:

#         N = len(grid)
#         M = len(grid[0])
#         answer = [[-2]*M for _ in range(N+1)]

#         for i in range(M):
#             answer[N][i] = i

#         def find_end(i,j):
#             if answer[i][j] == -2:
#                 if j < M-1 and grid[i][j] == 1 and grid[i][j+1] == 1:
#                     answer[i][j] = find_end(i+1,j+1)
#                 elif j > 0 and grid[i][j] == -1 and grid[i][j-1] == -1:
#                     answer[i][j] = find_end(i+1,j-1)
#                 else:
#                     answer[i][j] = -1
#             return answer[i][j]

#         for j in range(M):
#             find_end(0,j)

#         return answer[0]


if __name__ == "__main__":
    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
    ans = [1, -1, -1, -1, -1]
    output = Solution().findBall(grid)
    print(output)
