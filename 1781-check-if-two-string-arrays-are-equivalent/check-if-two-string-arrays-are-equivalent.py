class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:

        n = len(word1)
        m = len(word2)
       
        i = 0
        j = 0
        w1i = 0
        w2j = 0

        while w1i < n and w2j < m:

            if word1[w1i][i] != word2[w2j][j]:
                return False
            
            i += 1
            j += 1
            
            if i == len(word1[w1i]):
                i = 0
                w1i += 1
            
            if j == len(word2[w2j]):
                j = 0
                w2j += 1

            if w1i == n and w2j == m:
                return True
        

        return False
        