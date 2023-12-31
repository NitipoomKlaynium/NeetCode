#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    for (int first = 0 ; first < nums.size() - 1; first++) {
        for (int second = first + 1 ; second < nums.size() ; second++) {
            if (nums[first] + nums[second] == target) {
                vector<int> result = {first, second};
                return result;
            }
        }
    }
    vector<int> result = {-1, -1};
    return result;
}

int main() {
    vector<int> vec{2, 3, 4};
    vector<int> result = twoSum(vec, 9);

    for(int item: result) {
        cout << item << " ";
    }
    return 0;
}
