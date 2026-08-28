#include<bits/stdc++.h>

using namespace std;

const int M = 1e9 + 7;

int modulo(long long base, long long exp){
    if(exp == 0){
        return 1;
    }

    if(exp == 1){
        return base;
    }

    long long unsigned int modulated = modulo(base, floor(exp/2)) % M;
    modulated = (modulated * modulated) % M;
    if(exp % 2 == 1)
        modulated = (modulated * base) % M;
    return modulated;
}

int main(){
    int T;
    long long a, b;

    cin >> T;

    for(int i = 0; i < T; i++){
        cin >> a >> b;

        // Fermat's little theorem
        b = b % (M-1);

        cout << modulo(a, b) << endl;
    }

    return 0;
}
