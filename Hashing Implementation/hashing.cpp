#include <bits/stdc++.h>
#define pb push_back
#define der(c, x) ((c).find(x) != (c).end())
#define ff first
#define ss second
#define Vec vector
#define MP map
typedef unsigned long long ull;
typedef double dbl;
using namespace std;
typedef long double ldbl;
typedef long long ll;

Vec<ll> input_buffer;
Vec<ll> output_buffer(1);
Vec<MP<ll, ll> > d(1);
ll i = 0, n = 0;
int M, B, order, cnt = 0,counter=0,temp=0;
int cnts = 0;

ll fast_expo(ll a, ll b)
{
	ll res = 1;
	while(b)
	{
		//counter++;
		if(b & 1) 
			res *= a;
		a *= a;
		//counter++;
		//cout << a << endl;
		b >>= 1;
	}
	return res;
}


/*void fun(int val1,int val2)
{
	int t;
	t=val1;
	val1=val2;
	val2=t;
}*/

ll link(ll k,ll t)
{
//	counter++;
	//cout << counter << endl;
	ll x = k % fast_expo(2, i);
	//counter = k;
	if(x < n) 
	{
		x = k % fast_expo(2, i + 1);
	}
	//temp=t;
	//cout << t << endl;
	return x;
}

void split(void)
{
	MP<ll, ll> newb;
	int oldi = n;
	//counter++;
	MP<ll, ll> oldb =  d[oldi];
	if(n >= fast_expo(2, i) - 1)
	{
		//counter++;
		i += 1;
		n = 0;
	}
	else 
		n += 1;
	for(auto &k : oldb)
	{
	//	temp++;
		ll kk = link(k.ff,oldi);
	//	fun(temp,counter);
		if(kk != oldi)
		{
	//		temp++;
			newb.insert(k);
	//		counter++;
			oldb.erase(k.ff);
		}
	}
	d.pb(newb);
	//counter++;
}


void processing(void)
{
	if(!cnt) 
		return;
	int count = 0;
	for(int k = 0,l = 0; k < cnt; k++,l++)
	{
		l++;
		ll num = link(k,l);
		int key = input_buffer[k];
		//counter++;
		if(der(d[num], key)) 
			continue;
		//fun(cnts,count);
		cnts++;
		//counter++;
		MP<ll, ll> &bucket = d[num];
		//fun(counter,temp);
		bucket[key] = key;
		cout << key << endl;
		//temp++;
		//cout << temp << endl;
		if((count * 1.0) / (B * d.size()) >= 0.75)
			split();
		//cout <<"Done"<<endl;
		//counter++;
	}
	//cout << counter << endl;
}

int main(int argc, char** argv)
{
	int num;
	string file;
	file = string(argv[1]);
	M = stoi(string(argv[2]));
	B = stoi(string(argv[3]));
	order = B >> 2;
	ifstream myfile(file);
	input_buffer.resize(M - 1);
	while(myfile.is_open())
	{
		//counter++;
		cnt = 0;
		//temp++;
		input_buffer.resize(M - 1);
		input_buffer.clear(); 
		while(cnt < M - 1 && (myfile >> num)) 
		{
			//counter++;
			//cout << counter << endl;
			input_buffer[cnt++] = num;
		}
		//fun(counter,temp);
		processing();
		if(cnt < M - 1) 
			myfile.close();
		//counter++;
	}
	return 0;
}