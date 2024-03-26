#include <iostream>
#include <vector>
using namespace std;

void run_case() {
    int N, K, W; 
    cin >> N >> K >> W;
    vector<int>dp(N + 1, 0), dp2 = dp;
    vector<int>psa(N + 1, 0);
    for(int i = 1; i <= N; i++) {
        cin >> psa[i];
        psa[i] += psa[i - 1];
    }
    for(int i = 1; i <= K; i++) {
        for(int j = 1; j <= N; j++) {
            dp2[j] = max(dp2[j - 1], dp[max(0, j - W)] + psa[j] - psa[max(0, j - W)]);
        }
        swap(dp, dp2);
    }
    cout << dp[N] << endl;
}

int main(){
    int T; cin >> T;
    while(T--) {
        run_case();
    }
}