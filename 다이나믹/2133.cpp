#include <iostream>
using namespace std;

int main(void){
    int dp[1000] = {0, };
    int input = 0;
    cin >> input;

    dp[2] = 3;
    for (int i = 3; i <= input; i++){
        if (i % 2 == 0){    // 짝수인경우
            if (i % 4 == 0){    // 4의 배수인경우
                dp[i] = dp[i - 2] * 3 + 2;
            }
            else{
                dp[i] = dp[i-2] * 3;
            }
        }
        else{
            dp[i] = 0;
        }
    }
    cout << dp[input];
}

// #include <iostream>
// #include <string>
// #include <vector>
 
// #define MODULER 1000000007
// using namespace std;
 
// int solution(int n) 
// {
//     if(n % 2 == 1) return 0;
//     long long DP[5010] = { 0, };
//     DP[0] = 1;
//     DP[2] = 3;
//     for(int i = 4; i <= n ; i = i + 2)
//     {
//         DP[i] = DP[i - 2] * 3;
//         for(int j = i - 4; j >= 0 ; j = j - 2)
//         {
//             DP[i] = DP[i] + DP[j] * 2;
//         }
//         DP[i] = DP[i] % MODULER;
//     }
    
//    return (int)DP[n];
// }

// int main(void){
//     cout << solution(100);
// }