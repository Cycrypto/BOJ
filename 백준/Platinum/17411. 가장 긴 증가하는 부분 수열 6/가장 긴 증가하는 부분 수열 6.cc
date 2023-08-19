#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#define indexL(i) i*2
#define indexR(i) i*2+1
#define Len first
#define Cnt second
using namespace std;

const int maxN = 2000000000;
const int Mod = 1000000007;
typedef pair<int, int> Pair;

Pair myMax(Pair L, Pair R)
{
	if (L.Len == R.Len) return Pair(L.Len, (L.Cnt + R.Cnt) % Mod);
	if (L.Len < R.Len) return R;
	if (L.Len > R.Len) return L;
}

void Coordinate_compression(vector<int>& arr)
{
	vector<int> Temp = arr;

	sort(Temp.begin(), Temp.end());

	for (int i = 1; i < Temp.size(); i++)
		if (Temp[i - 1] == Temp[i]) Temp[i - 1] = maxN;

	sort(Temp.begin(), Temp.end());

	for (int i = 0; i < arr.size() && arr[i] < maxN; i++)
		arr[i] = (lower_bound(Temp.begin(), Temp.end(), arr[i]) - Temp.begin()) + 1;
}

struct SegmentTree
{
	int Root, Depth, Size, Leaf;
	vector<Pair> SegArr;

	SegmentTree() :SegmentTree(0) {}
	SegmentTree(int nSize) :Root(1), Depth(ceil(log2(nSize)) + 1), Leaf(1 << (Depth - 1)), Size(1 << Depth) { SegArr.assign(Size, Pair(0, 0)); }

	void modify(int index, Pair& val)
	{
		if (SegArr[index].Len < val.Len) SegArr[index] = val;
		else if (SegArr[index].Len == val.Len) SegArr[index].Cnt = (SegArr[index].Cnt + val.Cnt) % Mod;
	}
	void update(int index, Pair val)
	{
		index += (Leaf - 1);
		modify(index, val);

		while (index > 1)
		{
			index /= 2;
			SegArr[index] = myMax(SegArr[indexL(index)], SegArr[indexR(index)]);
		}
	}

	Pair query(int obtL, int obtR) { return query(obtL, obtR, Root, 1, Leaf); }
	Pair query(int obtL, int obtR, int index, int curL, int curR)
	{
		if (curR < obtL || obtR < curL) return Pair(0, 0);
		if (obtL <= curL && curR <= obtR) return SegArr[index];

		int mid = (curL + curR) / 2;
		return myMax(query(obtL, obtR, indexL(index), curL, mid), query(obtL, obtR, indexR(index), mid + 1, curR));
	}
};


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int N;
	cin >> N;

	vector<int> arr(N);
	SegmentTree st(N);

	for (int i = 0; i < N; i++) cin >> arr[i];
	Coordinate_compression(arr);

	Pair answer(0, 0);
	for (int i = 0; i < N; i++)
	{
		Pair res;

		if (arr[i] == 1) res = Pair(1, 1);
		else
		{
			res = st.query(1, arr[i] - 1); 

			if (res == Pair(0, 0)) res = Pair(1, 1);
			else res.Len++;		
		}

		answer = myMax(answer, res);
		st.update(arr[i], res);
	}

	cout << answer.Len << ' ' << answer.Cnt << '\n';

	return 0;
}