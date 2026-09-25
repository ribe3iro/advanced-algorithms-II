#include<bits/stdc++.h>

using namespace std;

int m[1000];

struct Compare{
    bool operator()(pair<int, int> a, pair<int, int> b){
        return a.first / a.second < b.first / b.second;
    }
};


int main(){
    int N;
    cin >> N;
    for(int j = 0; j < N; j++){
        int p, n;
        cin >> p >> n;
        priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;
        int m;
        for(int i = 0; i < n; i++){
            cin >> m;
            pq.push({m, 1});
        }

        p -= n;
        for(int i=0; i<p; i++){
            int a; int b;
            tie(a, b) = pq.top(); pq.pop();
            pq.push({a, b+1});
        }

        int a; int b;
        tie(a, b) = pq.top();
        cout << ceil(a/b) << endl;
    }

    return 0;
}
