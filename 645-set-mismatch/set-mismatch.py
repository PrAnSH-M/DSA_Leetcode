class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        """
            take map where you store number and its freq and n will be used to see which number is missing 
            nums = [1,2,2,4]
            missing -> 3
            then chech map to see whose feq > 1
            dup-> 2
            output = [2,3]

        """

        # mp = {}
        # ans = []

        # for i in nums:
        #     mp[i] = mp.get(i, 0) + 1
        
        n = len(nums)
        # for i in range(1,n+1):
        #     # print(i)
        #     if i not in mp:
        #         ans.append(i)
        #     elif mp.get(i) > 1:
        #         # print(mp[i])
        #         ans.insert(0, i)
        
        # return ans

        """
            will iterate over array and do nums[i] = nums[abs(nums[i])-1]
            nums[i] * -1

            and if we found dup means that no cant be -ve means that is our dup and its index +1 will be missing number 
        """
       
        ans = []

        for i in range(n):
            idx = abs(nums[i]) - 1

            if nums[idx] < 0:
                # Duplicate number found
                ans.append(abs(nums[i]))
            else:
                nums[idx] *= -1

        for i in range(n):
            if nums[i] > 0:
                # Missing number found
                ans.append(i + 1)

        return ans
            

                
            
        