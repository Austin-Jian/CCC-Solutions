#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<pair<int, int>> factors(int num, int m, int n) {
    vector<pair<int, int>> pos;
    for (int i = 1; i * i <= num; i++) {
        if (num % i == 0) {
            if (i <= m && num / i <= n) {
                pos.push_back({i, num / i});
            }
            if (i <= n && num / i <= m && i != num / i) {
                pos.push_back({num / i, i});
            }
        }
    }
    return pos;
}

bool bfs(const vector<vector<vector<pair<int, int>>>> &adjList, int m, int n) {
    // Define the directions to move in the grid: up, down, left, right
    const vector<int> dx = {-1, 1, 0, 0};
    const vector<int> dy = {0, 0, -1, 1};

    // Queue for BFS
    queue<pair<int, int>> q;
    vector<vector<bool>> visited(m + 1, vector<bool>(n + 1, false));

    // Start from the first cell
    q.push({1, 1});
    visited[1][1] = true;

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        // Check if we reached the ending cell
        if (x == m && y == n) {
            return true;
        }

        // Explore all possible neighbors
        for (const auto &[nx, ny] : adjList[x][y]) {
            if (nx <= m && ny <= n && !visited[nx][ny]) {
                q.push({nx, ny});
                visited[nx][ny] = true;
            }
        }
    }

    // If the ending cell is not reachable
    return false;
}

int main() {
    int m, n;
    vector<vector<vector<pair<int, int>>>> adjList;
    cin >> m >> n;
    vector<vector<int>> values(m + 1, vector<int>(n + 1));
    adjList.resize(m + 1, vector<vector<pair<int, int>>>(n + 1));

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> values[i][j];
        }
    }

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            adjList[i][j] = factors(values[i][j], m, n);
        }
    }

    if (bfs(adjList, m, n)) {
        cout << "yes"<<endl;
    } else {
        cout << "no"<<endl;
    }

    return 0;
}