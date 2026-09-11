class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> history;

        for (int i = 0; i < nums.size(); i ++){
            int curr = target - nums[i];
            if (history.find(curr) != history.end()){
                return {history.find(curr) -> second, i};
            }
            else{
                history[nums[i]] = i;
            }
        }
    }
};
