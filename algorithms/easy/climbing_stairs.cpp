#include <vector>
class Solution {
public:
    int climbStairs(int n) {
        std::vector<int> distinctWays(n + 1, 0);
        distinctWays[0] = 1;

        for(int i = 0; i < n; i++) {
            distinctWays[i+1] += distinctWays[i];
            if(i + 2 < n + 1) {
                distinctWays[i+2] += distinctWays[i];
            }
        }
        return distinctWays[n];
    }
};