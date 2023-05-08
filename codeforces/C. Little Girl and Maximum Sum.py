#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
int n, q;
cin >> n >> q;
vector<int> nums(n);
for (int i = 0; i < n; i++) {
    cin >> nums[i];
}
sort(nums.rbegin(), nums.rend());

vector<int> prfxSum(n + 1, 0);
for (int i = 0; i < q; i++) {
    int start, end;
    cin >> start >> end;
    prfxSum[start - 1] += 1;
    prfxSum[end] -= 1;
}
for (int i = 1; i < prfxSum.size(); i++) {
    prfxSum[i] += prfxSum[i - 1];
}
sort(prfxSum.rbegin(), prfxSum.rend());

long long maxSum = 0;
for (int i = 0; i < n; i++) {
    if (prfxSum[i] == 0) {
        break;
    }
    maxSum += (long long) prfxSum[i] * nums[i];
}
cout << maxSum << endl;
return 0;
}
