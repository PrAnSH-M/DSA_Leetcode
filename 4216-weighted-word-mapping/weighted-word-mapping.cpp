class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        int n = words.size();
        int m = weights.size();

        string output = "";

        char reverse_alphabet[] = {
            'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q',
            'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
            'f', 'e', 'd', 'c', 'b', 'a'
        };

        for(int i=0; i<n;i++) {
            int sum = 0;

            for(char ch : words[i]) {
                sum += weights[ch - 'a'];
            }

            int idx = sum % 26;
            output += reverse_alphabet[idx];
        }

        return output;

    }
};