class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> res;

        for (string& s: strs){
            array<int, 26> count {};

            for (char c: s){
                count[c - 'a']++;
            }
            res[count].push_back(s);
        }
        vector<vector<string>> result;

        for (auto& [key, value]: res){
            result.push_back(value);
        }
        return result;
    }
};
