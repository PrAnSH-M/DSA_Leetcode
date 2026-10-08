class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        """
            in map we store (val of mat[i+j]) as key and correspond to that key
            we will store list of elements whose sum will be equal to key
            {
                0 : [1],
                1: [4,2],
                2: [7,5,3],
                3: [8,6],
                4: [9]
            }

            and then we will sort the list and put back them in mat in reverse 

        """

        mp = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = i + j

                if key not in mp:
                    mp[key] = []
                
                mp[key].append(mat[i][j])
            
        ans = []

        for key in mp:
            if key % 2 == 0:
                mp[key].reverse()
                print(mp[key])
            
            for val in mp[key]:
                ans.append(val)

        return ans

        
        