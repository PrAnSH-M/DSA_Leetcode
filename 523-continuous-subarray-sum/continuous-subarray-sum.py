class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
            will store a map of reminder -> idx
            then will calculate sum % k and store it in mp if not seen and if seen will check its size if its >= 2 return true else return false

            and if we found ans but its size is not >= 2 return false

        """

        mp = {0: -1}

        n = len(nums)

        sum = 0 # initial sum

        for i in range(n):
            sum += nums[i]
            rem = sum % k
            if rem not in mp:
                mp[rem] = i
            else:
                c = i - mp[rem]

                if c >= 2:
                    return True
            
        
        return False
            




        