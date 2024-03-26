#include <bits/stdc++.h>
using namespace std;

int n, m, ans = 0;
vector<string> a;

void dfs(int x, int y){
    if (x < 0 || x >= n || y < 0 || y >= m || a[x][y] == '*'){
        return;
    }
    if (a[x][y] == 'S'){
        ans += 1;
    }
    else if (a[x][y] == 'M'){
        ans += 5;
    }
    else if (a[x][y] == 'L'){
        ans += 10;
    }
    a[x][y] = '*';
    dfs(x+1,y);
    dfs(x-1,y);
    dfs(x,y + 1);
    dfs(x,y-1);
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    a.resize(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    int x, y;
    cin >> x >> y;
    dfs (x,y);
    cout << ans << endl;
}