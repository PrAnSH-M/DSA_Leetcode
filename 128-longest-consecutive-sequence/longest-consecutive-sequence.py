class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        # print(hashset)

        max_len = 0
        current_num = 0
        current_len = 0

        for num in hashset:
            if num - 1 not in hashset:
                current_num = num
                current_len = 1
            
            while current_num + 1 in hashset:
                current_len += 1
                current_num += 1
            
            max_len = max(max_len, current_len)

        return max_len

