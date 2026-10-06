class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closestSum = float('inf')
        for k in range(n-2):
            i = k+1
            j = n-1

            while(i < j):
                sol = nums[k]+nums[i]+nums[j]

                if abs(sol - target) < abs(target - closestSum):
                    closestSum = sol
                
                if sol < target:
                    i += 1

                else :
                    j -= 1
        return closestSum
        