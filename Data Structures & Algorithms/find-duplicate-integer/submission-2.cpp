class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        vector<bool> result (nums.size());

        for (int num: nums){
            if (result[num]){
                return num;
            }
            result[num] = true;
        }
    }
};
