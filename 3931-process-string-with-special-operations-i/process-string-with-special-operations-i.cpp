class Solution {
public:
    string processStr(string s) {
        int n = s.size();

        string result;

        for(int i=0; i<n;i++) {
            char ch = s[i];
            if (ch >= 'a' && ch <= 'z') {
                result += ch;
            }
            else if(ch == '*') {
                if(!result.empty()) {
                    // remove last char from result if not empty
                    result.pop_back();
                }

            }
            else if(ch == '#') {
                // duplicate the current result and append at last
                result += result;
            }

            else if(ch == '%') {
                // reverse the current result
                reverse(result.begin(), result.end());
            }
        }
        return result;
    }
};