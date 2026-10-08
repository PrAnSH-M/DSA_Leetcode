class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        """
            in map we store (val of mat[i-j]) as key and correspond to that key
            we will store list of elements whose sum will be equal to key
            {
                -3 : [1],
                -2: [1,2],
                -1: [3,1,2],
                 0: [3,2,1],
                 1: [2,1],
                 2: [1] 
            }

            and then we will sort the list and put back them in mat in reverse 

        """
        mp = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])-1, -1, -1):
                key = i-j # key will be the val of [i-j]

                if key not in mp:
                    mp[key] = []

                mp[key].append(mat[i][j]) # to store val correspond to key 

        
        print(mp)


        # sort every diagonal
        for key in mp:
            mp[key].sort()

        # put elem back
        for i in range(len(mat)):
            for j in range(len(mat[0])-1, -1, -1):
                key = i-j
                mat[i][j] = mp[key].pop(0) # pop from front
        
        return mat
                



        