#include <algorithm>
#include <vector>
#include <iostream>
#include <iterator>

using namespace std;


class Solution {
public:
    static int search(vector<int>& nums, int target) {
        long left = 0;
        long right = nums.size();

        while (left <= right) {
            long* center = (long*) malloc(sizeof(long));
            *center = left + (right - left) / 2;
            if (nums[*center] == target) {
                return *center;
            }
            if (nums[*center] < target) {
                left = *center + 1;
            }
            else {
                right = *center - 1;
            }
            free(center);
        }

        return -1;
    }
};

int main() {
    std::vector<int> vec = {5};
    cout << "Hello\n";
    cout << Solution::search(vec, -5) << endl;
    return 0;
}