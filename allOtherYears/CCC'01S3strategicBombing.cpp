#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<vector<char>> adjList(26);
bool visited[26];


bool dfs(char start){
    visited[start-'A'] = true;
    for (auto b: adjList[start-'A']){
        if (visited[b-'A'] == false){
            dfs(b);
        }
    }
    if(visited[1]==false){
        return false;
    }
    else{
        return true;
    }

}

int main(){
    vector<string> edges; //vector to see which nodes are connected
    while (1){
        string edge;
        cin>>edge;
        if (edge == "**"){
            break;
        }
        edges.push_back(edge);
    }

     //making the adj list
    for (int i = 0; i<edges.size();i++){
        char node1 = edges[i][0];
        char node2 = edges[i][1];
        adjList[node1-'A'].push_back(node2);
        adjList[node2-'A'].push_back(node1);
    }
    int counts = 0;
    for (int x = 0; x<edges.size(); x++){
        if(!adjList[x].empty()){
            counts++;
        }
    }
    vector<string> check;
    int roads = 0;
    for (int a = 0; a<adjList.size(); a++){
        for (int b = 0; b<adjList[a].size(); b++){
            char node1 = a + 'A';
            char node2 = adjList[a][b];
            vector<vector<char>> copy = adjList;
            adjList[node1 - 'A'].erase(remove(adjList[node1 - 'A'].begin(), adjList[node1 - 'A'].end(), node2), adjList[node1 - 'A'].end()); // Remove edge
            adjList[node2 - 'A'].erase(remove(adjList[node2 - 'A'].begin(), adjList[node2 - 'A'].end(), node1), adjList[node2 - 'A'].end()); 
            fill_n(visited, 26, false);
            
            if (!dfs('A')){
                string road1;
                road1+=node2;
                road1+= node1;
                string road2; 
                road2 += node1; 
                road2 += node2;

                int cnt1 = count(check.begin(),check.end(),road1);
                int cnt2 = count(check.begin(),check.end(),road2);
                if (cnt1 == 0 and cnt2 == 0){
                    for (int g = 0; g<edges.size();g++){
                        if (road1 == edges[g]){
                            cout<<edges[g]<<endl;
                            roads ++;
                            check.push_back(edges[g]);
                            break;
                        }
                        if(road2 == edges[g]){
                            cout<<edges[g]<<endl;
                            roads ++;
                            check.push_back(edges[g]);
                            break;
                        }
                    }
                }
            }
            adjList=copy;
        }
    }
    cout<<"There are " << roads << " disconnecting roads."<<endl;
    return 0;
}