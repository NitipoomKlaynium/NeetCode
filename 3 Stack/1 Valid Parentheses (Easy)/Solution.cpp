#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <stack>
#include <map>

using namespace std;

class Solution {
public:
    static bool isValid(string s) {
        
        stack<char> left;
        map<char, char> bracket = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (char c: s) {
            if (c == '(' || c == '[' || c == '{') {
                left.push(c);
            }
            else {
                if (left.size() == 0) return false;
                if (bracket[c] == left.top()) left.pop();
                else return false;                
            }
        }

        if (!left.empty()) return false;
        return true;
    }
};

int main() {
    string s = "(){[]{}";
    cout << Solution::isValid(s);
    return 0;
}