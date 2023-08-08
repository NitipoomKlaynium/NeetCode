#include <algorithm>
#include <vector>
#include <iostream>
#include <iterator>

using namespace std;

class Solution {
public:
    static int maxProfit(vector<int>& prices) {
        int min = prices[0];
        int maxProfit = 0;
        for (int price: prices) {
            int profit = price - min;
            if (profit > 0) {
                if (profit > maxProfit) maxProfit = profit;
            }
            else {
                min = price;
            }
            delete &profit;
        }
        return maxProfit;
    }
};

int main() {
    vector<int> vec = {7,6,4,3,1};
    cout << Solution::maxProfit(vec) << endl;
}