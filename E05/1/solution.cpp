#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int L, S;
        cin >> L >> S;

        vector<vector<long long>> dp(L + 1, vector<long long>(S + 1, 0));

        dp[0][0] = 1;

        for (int c = 1; c <= 26; c++) {
            for (int len = min(c, L); len >= 1; len--) {
                for (int sum = S; sum >= c; sum--) {
                    dp[len][sum] += dp[len - 1][sum - c];
                }
            }
        }

        cout << dp[L][S] << '\n';
    }

    return 0;
}
