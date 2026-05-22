class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {

        unordered_set<string> set;

        // store all prefixes of arr1
        for(int i = 0; i < arr1.size(); i++) {

            string s = to_string(arr1[i]);
            string prefix = "";

            for(int j = 0; j < s.size(); j++) {

                prefix += s[j];
                set.insert(prefix);
            }
        }

        int ans = 0;

        // check prefixes in arr2
        for(int i = 0; i < arr2.size(); i++) {

            string s = to_string(arr2[i]);
            string prefix = "";

            for(int j = 0; j < s.size(); j++) {

                prefix += s[j];

                if(set.find(prefix) != set.end()) {
                    ans = max(ans, j + 1);
                }
            }
        }

        return ans;
    }
};