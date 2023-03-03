//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution{
    bool ispossiable(vector<vector<int>> &m,vector<vector<int>> &vis, int n,int nx,int ny){
        return ( (nx>=0 && nx < n) && (ny>=0 && ny < n)&&(vis[nx][ny] == 0) && (m[nx][ny] == 1) );
    }
    void solve(vector<vector<int>> &m,vector<vector<int>> &vis,string &path, int n,int x,int y,vector<string> &ans){
        
        
        if((x == n-1) && (y == n-1)){
            ans.push_back(path);
            return;
        }
        vis[x][y] = 1;
        
        int nx,ny;
        
        //up
        nx = x-1;
        ny = y;
        if(ispossiable(m,vis,n,nx,ny)){
            path += 'U';
            solve(m,vis,path,n,nx,ny,ans);
            path.pop_back();
        }
        
        //down
        nx = x+1;
        ny = y;
        if(ispossiable(m,vis,n,nx,ny)){
            path += 'D';
            solve(m,vis,path,n,nx,ny,ans);
            path.pop_back();
        }
        
        //left
        nx = x;
        ny = y-1;
        if(ispossiable(m,vis,n,nx,ny)){
            path += 'L';
            solve(m,vis,path,n,nx,ny,ans);
            path.pop_back();
        }
        
        //right
        nx = x;
        ny = y+1;
        if(ispossiable(m,vis,n,nx,ny)){
            path += 'R';
            solve(m,vis,path,n,nx,ny,ans);
            path.pop_back();
        }
        
        
        vis[x][y] = 0;
    }
    public:
    vector<string> findPath(vector<vector<int>> &m, int n) {
        // Your code goes here
        
        vector<string> ans;
        
        if(m[0][0] == 0){
            return ans;
        }
        
        int x = 0;
        int y = 0;
        string path = "";
        
        vector<vector<int>> visited = m;
        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                visited[i][j] = 0;
            }
        }
        
        solve(m,visited,path,n,x,y,ans);
        
        sort(ans.begin(),ans.end());
        
        return ans;
        
    }
};

    


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> m(n, vector<int> (n,0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }
        Solution obj;
        vector<string> result = obj.findPath(m, n);
        sort(result.begin(), result.end());
        if (result.size() == 0)
            cout << -1;
        else
            for (int i = 0; i < result.size(); i++) cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends