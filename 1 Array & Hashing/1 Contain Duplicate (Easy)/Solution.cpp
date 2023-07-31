#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool containsDuplicate(vector<int>& nums) {

    sort(nums.begin(), nums.end());
    
    std::size_t i = 0;
    while(i < nums.size() - 1) {
        if (nums[i] == nums[++i]) {
            return true;
        }
    }

    return false;
}

int main() {
    std::vector<int> vec = {1, 2, 3, 1};
    cout << containsDuplicate(vec);
    return 0;
}

