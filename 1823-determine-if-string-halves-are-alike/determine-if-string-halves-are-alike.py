class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        n = len(s)

        first_half = n//2

        a = s[:first_half]
        b = s[first_half:]

        count_a = 0
        count_b = 0
        for ch in a:
            if ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u':
                count_a += 1
    
        for ch in b:
            if ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u':
                count_b += 1

        return count_a == count_b
        
        
        