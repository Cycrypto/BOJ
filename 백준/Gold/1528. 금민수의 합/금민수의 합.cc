#include <bits/stdc++.h>
using namespace std;
#define pii pair<int,int>
#define fr first
#define sd second
const int mx = 1000001;
int n;
vector<int>kms;
void dfs(string nn) {
	string a = nn + "4";
	string b = nn + "7";
	int A = stoi(a);
	int B = stoi(b);
	if (A <= n) {
		kms.push_back(A);
		dfs(a);
	}
	if (B <= n) {
		kms.push_back(B);
		dfs(b);
	}
}

vector<int> num[mx];
bool chk[mx];
int dp[mx];

void dfs2(int n) {
	if (n < 0)return;
	if (chk[n])return;
	chk[n] = true;
	for (auto& i : kms) {
		dfs2(n - i);
		if (n - i >= 0 && dp[n] > dp[n - i]+1) {
			dp[n] = dp[n - i] + 1;
			num[n] = num[n - i];
			num[n].push_back(i);
		}
		else if (n - i >= 0 && dp[n] == dp[n - i]+1 && num[n] > num[n - i]) {
			num[n] = num[n - i];
			num[n].push_back(i);
		}
	}
	sort(num[n].begin(), num[n].end());
}

int main() {
	ios::sync_with_stdio(0), cin.tie(0);
	cin >> n; dfs("");
	for (int i = 1; i <= n; ++i)dp[i] = 1e9;
	dfs2(n);
	if (dp[n] == 1e9) {
		cout << -1;
		return 0;
	}
	for (auto& i : num[n])cout << i << ' ';
}