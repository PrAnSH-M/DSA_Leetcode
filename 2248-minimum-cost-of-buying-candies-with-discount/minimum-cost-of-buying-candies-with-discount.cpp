class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(begin(cost), end(cost));

        int n = cost.size();
        int total_cost = 0;

        int cnt = 0;

        for(int i = n - 1; i >= 0; i--) {

            cnt++;

            if(cnt == 3) {
                cnt = 0;      // free candy
                continue;
            }

            total_cost += cost[i];
        }

        return total_cost;
    }
};