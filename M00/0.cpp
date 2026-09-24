#include<bits/stdc++.h>

using namespace std;

int m[1000];

struct Compare{
    bool operator()(pair<float, int> a, pair<float, int> b){
        if (a.first != b.first){
            return a.first < b.first;
        }

        return a.second > b.second;
    }
};

priority_queue<pair<float, int>, vector<pair<float, int>>, Compare> pq;

int main(){
    int p, n;
    while(cin >> p >> n){
        float m;
        for(int i = 0; i < n; i++){
            cin >> m;
            pq.push({m, 1});
        }

        p -= n;
        for(int i=0; i<p; i++){
            float a; int b;
            tie(a, b) = pq.top(); pq.pop();
            a = (a*b)/++b;
            pq.push({a, b});
        }

        cout << ceil(pq.top().first) << endl;
    }

    return 0;
}
