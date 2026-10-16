#include <iostream>
#include <cmath>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        long long N;
        cin >> N;

        long long r = sqrtl(N);

        if (r * r == N) {
            cout << "ativada\n";
        } else {
            cout << "desativada\n";
        }
    }

    return 0;
}
