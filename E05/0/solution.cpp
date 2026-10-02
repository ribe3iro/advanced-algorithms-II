#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    vector<int> queries(T);

    int maxN = 0;

    for (int i = 0; i < T; i++) {
        cin >> queries[i];
        maxN = max(maxN, queries[i]);
    }

    vector<int> dp(maxN + 1, maxN + 1);
    dp[0] = 0;

    for (int n = 1; n <= maxN; n++) {
        for (int i = 1; i * i <= n; i++) {
            dp[n] = min(dp[n], dp[n - i * i] + 1);
        }
    }

    for (int n : queries) {
        cout << dp[n] << '\n';
    }

    return 0;
}
