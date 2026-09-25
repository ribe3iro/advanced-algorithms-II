#include<bits/stdc++.h>

using namespace std;

bool bs(int* arr, int val, int lower, int upper){
	if(lower > upper){
		return false;
	}
	
	int middle = (lower + upper)/2;
	
	if(arr[middle] == val){
		return true;
	}
	if(arr[middle] > val){
		upper = middle-1;
	}
	if(arr[middle] < val){
		lower = middle+1;
	}
	
	return bs(arr, val, lower, upper);
	
}

int main(){
    int N;
    cin >> N;
    for(int j = 0; j < N; j++){
        int x[(long)1e6+5];
        long long n, m, a, c;
        cin >> n >> m >> a >> c >> x[0];

        for(int i = 1; i <= n; i++){
            x[i] = (a * x[i-1] + c) % m;
        }
		
		int count = 0;
		for(int i = 1; i <= n; i++){
			if(bs(x, x[i], 1, n))
				count++;
        }
		
		cout << count << endl;
    }

    return 0;
}
