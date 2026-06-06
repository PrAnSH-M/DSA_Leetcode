class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        sort(asteroids.begin(), asteroids.end());
        long long currentMass = mass;
        bool all_destroid = false;

        for(int i = 0; i < asteroids.size(); i++) {
            if(asteroids[i] <= currentMass) {
                currentMass += asteroids[i];
            }
            else {
                return false;
            }
        }

        return true;

    }
};