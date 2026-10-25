class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        array = [0]*26

        # filling array
        for charac in sentence:
            index = ord(charac) - ord('a')
            array[index] = 1

        return sum(array) == 26

        