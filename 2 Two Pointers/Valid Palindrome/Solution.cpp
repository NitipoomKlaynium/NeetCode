#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    static bool isPalindrome(string s) {
        string::iterator left = s.begin();
        string::iterator right = s.end();

        while (left < right) {
            if (!iswalnum(*left)) {
                left++;
                continue;
            }
            if (!iswalnum(*right)) {
                right--;
                continue;
            }
            if (tolower(*left) == tolower(*right)) {
                left++;
                right--;
            }
            else {
                return false;
            }
        }
        return true;
    }
};

int main() {
    string s = "A man, a plan, a canal: Panama";
    cout << Solution::isPalindrome(s);
    return 0;
}