class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_set<int> seen;
        for(int i{0}; i < nums.size(); i++){
            for(int j{0}; j < i; j++){
                if ((nums[i] + nums [j]) == target) {

                    return std::vector<int> {j, i};
                } 
            }
        }
        return {0, 0};
    }

    //if 5 is on 1 index it will repeat ? so maybe separate counter ? 
};