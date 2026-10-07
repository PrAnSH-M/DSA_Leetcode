class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])

        top = 0
        down = n-1
        left =0
        right = m-1

        final_arr = []

        while top <= down and left <= right:


            # first print top so our top will be fixed
            for i in range(left, right+1):
                final_arr.append(matrix[top][i])
            
            top+=1 # move top to next row

            # right print so our right will be fixed
            for i in range(top, down+1):
                final_arr.append(matrix[i][right])
            
            right -= 1 # move right to prev colum

            # now will print from right to left
            if top <= down:
                for i in range(right, left-1, -1):
                    final_arr.append(matrix[down][i])
                down -=1

            # now down to up
            if left <= right:
                for i in range(down, top-1, -1):
                    final_arr.append(matrix[i][left])
                left += 1

        
        return final_arr


