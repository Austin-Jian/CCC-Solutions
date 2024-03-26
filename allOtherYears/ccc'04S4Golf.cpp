#include <iostream>
#include <vector>
using namespace std;

int main(){
    int d, nc; cin >> d >> nc;
    vector<int>c(nc, 0);
    for(int &x: c) cin >> x;

    vector<int>dp(d + 1, 2e9);
    for(int x: c) dp[x] = 1;

    for(int i = 1; i <= d; i++) {
        for(int x: c) {
            if(i - x < 0) continue;
            dp[i] = min(dp[i], dp[i - x] + 1);
        }
    }
    if(dp[d] == 2e9) {
        cout << "Roberta acknowledges defeat." << endl;
    } else {
        cout << "Roberta wins in " << dp[d] << " strokes." << endl;
    }
}
