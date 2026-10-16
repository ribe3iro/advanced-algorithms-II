#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        string N;
        cin >> N;

        int sum = 0;

        for (char digit : N) {
            sum += digit - '0';
        }

        if (sum % 9 != 0) {
            cout << 0 << '\n';
            continue;
        }

        int degree = 1;

        while (sum != 9) {
            int next_sum = 0;

            while (sum > 0) {
                next_sum += sum % 10;
                sum /= 10;
            }

            sum = next_sum;
            degree++;
        }

        cout << degree << '\n';
    }

    return 0;
}
