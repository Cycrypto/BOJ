#include <iostream>
using namespace std;

long long D[91];//n�� 90�����̹Ƿ� 0~90����
int n;//n��° �Ǻ���ġ ��
//�Ǻ���ġ �Լ�, n����� �� �Ǻ���ġ ���� ���� D�迭
long long fibo(int n, long long D[90])
{
	//�Ǻ���ġ ���� D[i] = D[i - 1] + D[i - 2]�̹Ƿ�
	//1��°�� 2��°�� �������־�� 3��°���� ��� ����
	D[0] = 0;//�Ǻ���ġ 1��°
	D[1] = 1;//�Ǻ���ġ 2��°
	for (int i = 2; i <= n; i++)//�Ǻ���ġ 3��°���� ����
	{
		D[i] = D[i - 1] + D[i - 2];
	}
	return D[n];//n��° �Ǻ���ġ�� ���
}

int main()
{
	cin >> n;
	printf("%lld", fibo(n, D));//n��° �Ǻ���ġ�� ���
	return 0;
}