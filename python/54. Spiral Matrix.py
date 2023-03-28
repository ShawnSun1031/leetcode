# class Solution:
#     def spiralOrder(self, matrix):
#         def correct_directions(r, c, pattern):
#             if pattern == 0:
#                 c -= 1
#                 r += 1
#             elif pattern == 1:
#                 r -= 1
#                 c -= 1
#             elif pattern == 2:
#                 c += 1
#                 r -= 1
#             elif pattern == 3:
#                 r += 1
#                 c += 1
#             pattern += 1
#             return r, c, pattern
#         rows = len(matrix)
#         cols = len(matrix[0])
#         # sequence :  col+1 -> row+1 -> col-1 -> row-1 -> col+1
#         ans = []
#         r, c, pattern = 0, 0, 0
#         for _ in range(rows*cols):
#             ans.append(matrix[r][c])
#             matrix[r][c] = True
#             if pattern == 0:
#                 c += 1
#             elif pattern == 1:
#                 r += 1
#             elif pattern == 2:
#                 c -= 1
#             elif pattern == 3:
#                 r -= 1

#             if (r == rows) | (c == cols) | (r == -1) | (c == -1):
#                 r, c, pattern = correct_directions(r, c, pattern)
#             elif (r < rows) & (c < cols):
#                 if matrix[r][c] == True:
#                     r, c, pattern = correct_directions(r, c, pattern)
#             if pattern == 4:
#                 pattern = 0

#         return ans

class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        res = []
        while left <= right and top <= bottom:
            #  top left to top right
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1
            # top right to right bottom
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1
            # right bottom to right left
            for col in range(right, left-1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
            # left bottom to top left
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            left += 1
        # just ignore the redundant and return length of m*n
        return res[:m*n]


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    ans = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    output = Solution().spiralOrder(matrix)
    print(output)
