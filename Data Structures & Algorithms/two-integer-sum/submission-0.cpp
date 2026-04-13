class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> sums;

        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];
            if (sums.find(diff) != sums.end()) {
                return {sums[diff], i};
            }
            sums.insert({nums[i], i});
        }
        return {};    
    }
};
