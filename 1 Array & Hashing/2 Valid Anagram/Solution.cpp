#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    static bool isAnagram(string s, string t) {

        if (s.size() != t.size()) return false;

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        for (int i = 0 ; i < s.size() ; i++) {
            if (s[i] != t[i]) return false;
        }

        return true;
    }
};

int main() {
    cout << Solution::isAnagram("abc", "bac");
    return 0;
}
