#include<iostream>

using namespace std;
int main() {
    int a[5] = {0, 0, 0, 0, 0};
    int i = 1;
    cout << a[0] << " " << a[1] << " "  << a[2] << " "  << a[3] << " "  << a[4] <<  "  i: " << i << endl;
    a[i++] = a[i++] = i++;
    cout << a[0] << " " << a[1] << " "  << a[2] << " "  << a[3] << " "  << a[4] << "  i: " << i << endl;

    return 0;
}