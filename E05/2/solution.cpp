#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, n;
    cin >> t >> n;

    vector<int> d(n), v(n), cost(n);

    for (int i = 0; i < n; i++) {
        cin >> d[i] >> v[i];
        cost[i] = 3 * d[i];
    }

    // dp[i][j] = maior quantidade de moedas usando
    // os primeiros i tesouros com j unidades de energia.
    vector<vector<int>> dp(n + 1, vector<int>(t + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int energy = 0; energy <= t; energy++) {
            // Não resgatar o tesouro i - 1.
            dp[i][energy] = dp[i - 1][energy];

            // Resgatar o tesouro i - 1, se houver energia suficiente.
            if (cost[i - 1] <= energy) {
                dp[i][energy] = max(
                    dp[i][energy],
                    dp[i - 1][energy - cost[i - 1]] + v[i - 1]
                );
            }
        }
    }

    // Reconstrução da solução.
    vector<int> chosen;

    int energy = t;

    for (int i = n; i >= 1; i--) {
        if (dp[i][energy] != dp[i - 1][energy]) {
            chosen.push_back(i - 1);
            energy -= cost[i - 1];
        }
    }

    reverse(chosen.begin(), chosen.end());

    cout << dp[n][t] << '\n';
    cout << chosen.size() << '\n';

    for (int i : chosen) {
        cout << d[i] << ' ' << v[i] << '\n';
    }

    return 0;
}
