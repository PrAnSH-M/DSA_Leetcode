class Solution {
public:
    int numberOfSpecialChars(string word) {
        
        unordered_map<char, int> mp;

        for (auto &ch : word) {
            mp[ch]++;
        }

        int count = 0;

        for (char ch = 'a'; ch <= 'z'; ch++) {
            if (mp.count(ch) && mp.count(ch - 'a' + 'A')) {
                count++;
            }
        }

        return count;
        
    }
};