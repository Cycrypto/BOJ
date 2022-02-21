#include <iostream>
using namespace std;

int main(void){
    int dp[1001] = {0, };
    int input = 0;
    cin >> input;   // 입력받는 부분

    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= input; i++){
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
    }
    cout << dp[input];
}