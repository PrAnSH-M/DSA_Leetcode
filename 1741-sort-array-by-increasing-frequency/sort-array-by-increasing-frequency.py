class Solution:
    
    def quick_sort(self, nums:list) -> list:
        if len(nums) <= 1:
            return nums

        P = nums[-1]

        L = [x for x in nums[:-1] if x[1] < P[1] or (x[1] == P[1] and x[0] > P[0])]
        R = [x for x in nums[:-1] if x[1] > P[1] or (x[1] == P[1] and x[0] < P[0])]

        L = self.quick_sort(L)
        R = self.quick_sort(R)

        return L + [P] + R
    
    def frequencySort(self, nums: list[int]) -> list[int]:
        mp = {}

        for i in nums:
            mp[i] = mp.get(i, 0) + 1

        elem = mp.keys()
        freq = mp.values()

        paired = list(zip(elem, freq))

        paired = self.quick_sort(paired)

        result = []

        for elem, freq in paired:
            for _ in range(freq):
                result.append(elem)

        return result