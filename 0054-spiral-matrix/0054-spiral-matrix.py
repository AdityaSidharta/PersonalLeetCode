class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if isinstance(matrix[0], int):
            return matrix
        elif len(matrix[0]) == 1 :
            return [matrix[i][0] for i in range(len(matrix))]
        else:
            output = []

            top = 0
            left = 0
            bottom = len(matrix) - 1
            right = len(matrix[0]) - 1
            
            bottom_top = bottom - top
            right_left = right - left

            while bottom_top > 0 and right_left > 0:
                for idx in range(left, right + 1):
                    output.append(matrix[top][idx])
                for idx in range(top + 1, bottom + 1):
                    output.append(matrix[idx][right])
                for idx in range(right - 1, left - 1, -1):
                    output.append(matrix[bottom][idx])
                for idx in range(bottom -1, top, -1):
                    output.append(matrix[idx][left])
                top = top + 1
                left = left + 1
                right = right - 1
                bottom = bottom - 1
                bottom_top = bottom - top
                right_left = right - left
                print(top)
                print(left)
                print(right)
                print(bottom)
                print(bottom_top)
                print(right_left)
                print('---')

            if bottom_top > 0 and right_left == 0:
                for idx in range(top, bottom + 1):
                    output.append(matrix[idx][left])
            if right_left > 0 and bottom_top == 0:
                for idx in range(left, right + 1):
                    output.append(matrix[top][idx])
            if bottom_top == 0 and right_left == 0:
                output.append(matrix[top][left])
            return output
