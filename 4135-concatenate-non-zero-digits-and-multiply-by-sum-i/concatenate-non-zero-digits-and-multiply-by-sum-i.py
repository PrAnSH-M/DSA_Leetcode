class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_zero_num = ""

        for dig in str(n):
            if dig != "0":
                non_zero_num += dig

        if non_zero_num == "":
            return 0
            
        non_zero_num = int(non_zero_num)
        
        sum_of_non_zero_dig = 0

        for dig in str(non_zero_num):
            sum_of_non_zero_dig += int(dig)

        return non_zero_num * sum_of_non_zero_dig
