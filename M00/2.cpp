#include<bits/stdc++.h>

using namespace std;

int solve(unordered_map<int, unordered_map<int, int>> adj_list, int* ref, int node){
	if(adj_list[node].size() <= 1){
		return 0;
	}
	
	unordered_map<int, int> neighborhood = adj_list[node];
	for(auto[neighbor, weight] : neighborhood){
		int value = 0;
		if(count(ref.begin(), ref.end(), neighbor) > 0){
			value = weight;
		}
	}
}

int main(){
	int CASES;
	cin >> CASES;
	for(int c = 0; c < CASES; c++){
		int N, F;
		cin >> N >> F;
		unordered_map<int, unordered_map<int, int>> adj_list;
		for(int i = 0; i < N-1; i++){
			int a, b, w;
			cin >> a >> b >> w;
			if(a < b){
				adj_list[a][b] = 0;
				adj_list[b][a] = w;
			}else{
				adj_list[a][b] = w;
				adj_list[b][a] = 0;
			}
		}
		
		int ref[(int)1e5+5];
		for(int i = 0; i < F; i++){
			cin >> ref[i];
		}
		
		cout << solve(adj_list, ref, 1) << endl;
		
	}

    return 0;
}
