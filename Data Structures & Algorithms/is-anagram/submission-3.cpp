class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        vector<int> count(26);
        
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a'] += 1;
            count[t[i] - 'a'] -= 1;
        }

        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }

        return true;
    }
};
