#include <iostream>
using namespace std;

long long D[91];//n이 90까지이므로 0~90까지
int n;//n번째 피보나치 수
//피보나치 함수, n번재와 각 피보나치 값을 넣을 D배열
long long fibo(int n, long long D[90])
{
	//피보나치 식이 D[i] = D[i - 1] + D[i - 2]이므로
	//1번째와 2번째는 정의해주어야 3번째부터 사용 가능
	D[0] = 0;//피보나치 1번째
	D[1] = 1;//피보나치 2번째
	for (int i = 2; i <= n; i++)//피보나치 3번째부터 정의
	{
		D[i] = D[i - 1] + D[i - 2];
	}
	return D[n];//n번째 피보나치값 출력
}

int main()
{
	cin >> n;
	printf("%lld", fibo(n, D));//n번째 피보나치값 출력
	return 0;
}