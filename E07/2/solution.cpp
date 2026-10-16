#include <iostream>
using namespace std;
using ll = long long;

ll extended_gcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }

    ll x1, y1;
    ll g = extended_gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

// Arredondamento para baixo, inclusive quando a e negativo; b deve ser positivo.
ll floor_div(ll a, ll b) {
    ll q = a / b;
    ll r = a % b;
    if (r != 0 && a < 0) {
        --q;
    }
    return q;
}

ll ceil_div(ll a, ll b) {
    return -floor_div(-a, b);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        ll N, c1, n1, c2, n2;
        cin >> N >> c1 >> n1 >> c2 >> n2;

        ll x, y;
        ll g = extended_gcd(n1, n2, x, y);

        if (N % g != 0) {
            cout << "sem solucao\n";
            continue;
        }

        // Uma solucao particular de n1*x + n2*y = N.
        x *= N / g;
        y *= N / g;

        // Todas as solucoes sao:
        // x = x0 + step_x*t; y = y0 - step_y*t.
        ll step_x = n2 / g;
        ll step_y = n1 / g;

        // Impoe x >= 0 e y >= 0 para obter o intervalo de t.
        ll lower = ceil_div(-x, step_x);
        ll upper = floor_div(y, step_y);

        if (lower > upper) {
            cout << "sem solucao\n";
            continue;
        }

        // Custo(t) = c1*x + c2*y; sua inclinacao e constante.
        ll slope = c1 * step_x - c2 * step_y;
        ll t;
        if (slope > 0) {
            t = lower;  // O custo cresce com t.
        } else if (slope < 0) {
            t = upper;  // O custo diminui com t.
        } else {
            t = lower;  // Todos os valores viaveis tem o mesmo custo.
        }

        x += step_x * t;
        y -= step_y * t;
        cout << x << ' ' << y << '\n';
    }

    return 0;
}
