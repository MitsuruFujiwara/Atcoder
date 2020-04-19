#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pint pair<int, int>
#define plint pair<ll, ll>
#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i,n) for (int i = 0; i < (n); ++i)
const int INF = 100100100;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-9;
#define SIZE 3
int main(){
    int n;
    bool is_bingo = false;
    vector<vector<int>> a(3,vector<int>(3));
    REP(i,SIZE) cin >> a[0][i];
    REP(i,SIZE) cin >> a[1][i];
    REP(i,SIZE) cin >> a[2][i];
    cin >> n;
    vector<int> b(n);
    REP(i,n) cin >> b[i];

    REP(i,n){
        REP(j,SIZE){
            REP(k,SIZE){
                if(a[k][j]==b[i]) a[k][j] = 0;
            }
        }
    }
    // yoko
    REP(i,SIZE){
        if(a[i][0]==0 && a[i][1]==0 && a[i][2]==0){
            cout << "Yes" << endl;
            return 0;
        }
    }
    // tate
    REP(i,SIZE){
        if(a[0][i]==0 && a[1][i]==0 && a[2][i]==0){
            cout << "Yes" << endl;
            return 0;
        }
    }
    // naname
    if(a[0][0]==0 && a[1][1]==0 && a[2][2]==0){
            cout << "Yes" << endl;
            return 0;
    }
    if(a[0][2]==0 && a[1][1]==0 && a[2][0]==0){
            cout << "Yes" << endl;
            return 0;
    }
    cout << "No" << endl;
    return 0;
}
