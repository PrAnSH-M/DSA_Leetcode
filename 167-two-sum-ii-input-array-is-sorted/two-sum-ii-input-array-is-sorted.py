class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        # output = []

    #    [ 2,  7,  11,   15 ]
    #      i.             j

        while(i < j):
            # if sum is greater than target move left
            if numbers[i] + numbers[j] > target:
                j -= 1
            
            # if sum is smaller than target move right
            if numbers[i] + numbers[j] < target:
                i += 1
            
            # if sum is equal to target return index
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]

        return []
            