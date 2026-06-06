class Solution {
public:
    int numberOfSpecialChars(string word) {
        int n = word.length();
        int count = 0;
        vector<int> lastOccurenceOfSmallCharacter(26, -1);
        vector<int> firstOccurenceOfCapitalCharacter(26, -1);

        for(int i=0;i<n; i++) {
            if(islower(word[i])) {
                lastOccurenceOfSmallCharacter[word[i] - 'a'] = i;
            }
            else {
                if(firstOccurenceOfCapitalCharacter[word[i] - 'A'] == -1) {
                    firstOccurenceOfCapitalCharacter[word[i] - 'A'] = i; 
                }
            }
        }

        for(int i=0;i <26; i++) {
            if(lastOccurenceOfSmallCharacter[i] != -1 && firstOccurenceOfCapitalCharacter[i] != -1 && lastOccurenceOfSmallCharacter[i] < firstOccurenceOfCapitalCharacter[i]) {
                count++;
            }
        }

        return count;
    }
};