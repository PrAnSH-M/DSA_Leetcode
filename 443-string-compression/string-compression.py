class Solution:
    def compress(self, chars: list[str]) -> int:
        """
            # approach 1 (brute fore)

            what i am thinking is going to each character one by one and seeing if next char is same as current chars[i] if yes just append its count as 2 because current is same as next so 1 + 1 a2 and so on and at the return the len of new_s of compressed

            [ "a", "a" ,"b" ,"b" ,"c" ,"c" ,"c" ]
                                                i
                                             j

                    count 3, bresk

                     , len 6
        """

        # n = len(chars)
        # if n == 0:
        #     return 0

        # compressed_s = ""
        # i = 0

        # while i < n:
        #     count = 1

        #     for j in range(i + 1, n):
        #         if chars[i] == chars[j]:
        #             count += 1
        #         else:
        #             break

        #     compressed_s += chars[i]

        #     if count > 1:
        #         compressed_s += str(count)

        #     i += count

        # print(compressed_s)
        # # return len(compressed_s)


        """
            here will take two pointer index and i 
            index and i both at 0 index

            then will match i with next one and increment count until we see diff char
            will keep count of curr_char and its count 
            when we see diff char we will stop and place curr_char to index then index+=1 and then place count then index+=1 then will update curr_char with new char and count again to 1
            and at then end will return val of index as our len

        """ 

        n = len(chars)

        index = 0
        i = 0

        while i < n:
            curr_char = chars[i]
            count = 0

            # Count consecutive occurrences
            while i < n and chars[i] == curr_char:
                count += 1
                i += 1

            # Write the character
            chars[index] = curr_char
            index +=1

            #write the count

            if count > 1:
                for c in str(count):
                    chars[index] = c
                    index += 1

        return index
            




        