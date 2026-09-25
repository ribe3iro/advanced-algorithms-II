#include<bits/stdc++.h>

using namespace std;

int main(){
    int N;
    cin >> N;
    for(int j = 0; j < N; j++){
        int x[INT_MAX+2];
        int n, m, a, c;
        cin >> n >> m >> a >> c >> x[0];

        for(int i = 1; i <= n; i++){
            x[i] = (a * x[i-1] + c) % m;
        }
    }

    return 0;
}
