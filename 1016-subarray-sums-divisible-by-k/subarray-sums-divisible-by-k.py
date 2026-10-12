class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n = len(nums)

        """
            we will take mp where we store it like {reminder: count}

            if never seen in mp store rem and its count 
            and later if we saw rem thats already in mp then we will ++ res and count of  that rem in mp
            and if we come up across -ve rem then we will do 

            K(n-1) + K

            for ex if rem is -4 and K is 7 so its like rem will -4 + 7 which is 3

        """

        mp = {0: 1}
        sum = 0
        res = 0

        for i in range(n):
            sum += nums[i]

            rem = sum % k

            if rem not in mp:
                mp[rem] = mp.get(rem, 0)+1

            else:
                if rem < 0:
                    rem = rem + k
                res += mp[rem]
                mp[rem] += 1
        
        return res



        


        