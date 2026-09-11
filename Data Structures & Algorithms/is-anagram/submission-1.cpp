class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        vector<int> s_count(26), t_count(26);
        
        for (int i = 0; i < s.length(); i++) {
            s_count[s[i] - 'a'] += 1;
            t_count[t[i] - 'a'] += 1;
        }

        for (int i = 0; i < 26; i++) {
            if (s_count[i] != t_count[i]) {
                return false;
            }
        }

        return true;
    }
};
