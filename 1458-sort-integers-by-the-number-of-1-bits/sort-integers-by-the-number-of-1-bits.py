class Solution:

    def count_of_1_ofBit(self, arr:[list]) -> list[int]:

        n = len(arr)
        bits = []
        for num in arr:
            binary = ""
            while num > 0:
                rem = num % 2
                binary = str(rem) + binary
                num //= 2
            counts = binary.count('1')
            bits.append(counts)
        return bits

    def quick_sort(self, arr:list) -> list:
        if len(arr) <= 1:
            return arr

        P = arr[-1]

        L = [
            x for x in arr[:-1]
            if x[1] < P[1] or (x[1] == P[1] and x[0] < P[0])
        ]

        R = [
            x for x in arr[:-1]
            if x[1] > P[1] or (x[1] == P[1] and x[0] >= P[0])
        ]

        L = self.quick_sort(L)
        R = self.quick_sort(R)

        return L + [P] + R

    def sortByBits(self, arr: list[int]) -> list[int]:

        bits_list = self.count_of_1_ofBit(arr)

        paired = list(zip(arr, bits_list))

        paired = self.quick_sort(paired)


        return [num for num, bits in paired]
            

