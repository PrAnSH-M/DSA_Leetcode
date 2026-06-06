class Solution {
public:

    int sumOfDigits(int num) {
        int sum = 0;

        while(num > 0) {
            sum += num % 10;
            num /= 10;
        }

        return sum;
    }

    int minElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;

        int sum_of_dig = 0;

        for(int i=0;i<n; i++) {
            int ans_for_current_idx = sumOfDigits(nums[i]);
            ans.push_back(ans_for_current_idx);
        }

        int small = ans[0];

        for(int i = 0; i<ans.size(); i++) {
            // store small elm;
            if(ans[i] < small) {
                small = ans[i];
            }
        }

        return small;
    }
};