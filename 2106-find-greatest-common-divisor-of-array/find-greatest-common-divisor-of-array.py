class Solution:

    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

    def findGCD(self, nums: List[int]) -> int:
        mini = nums[0]
        maxi = nums[0]

        for i in range(len(nums)):
            if nums[i] < mini:
                mini = nums[i]
            elif nums[i] > maxi:
                maxi = nums[i]

        return self.gcd(mini, maxi)
        
    
            
            