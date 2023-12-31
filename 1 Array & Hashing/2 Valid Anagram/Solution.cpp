#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool isAnagram(string s, string t) {

    if (s.size() != t.size()) return false;

    sort(s.begin(), s.end());
    sort(t.begin(), t.end());

    for (int i = 0 ; i < s.size() ; i++) {
        if (s[i] != t[i]) return false;
    }

    return true;
}


int main() {
    cout << isAnagram("abc", "bac");
    return 0;
}
