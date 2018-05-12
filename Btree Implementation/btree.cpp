#include <bits/stdc++.h>
#define endl '\n'
#define inf INT_MAX
#define pb push_back
#define ff first
#define ss second
#define Vec vector
#define L list
#define Pi pair
typedef long double ldbl;
using namespace std;

typedef unsigned long long ull;
typedef double dbl;
typedef long long ll;

int M, B, order, cnt = 0;
ull counter=0,temp=0;

Vec<int>output_buffer(1);

Vec<Pi<char, Pi<int, int> > > input_buffer;


typedef struct btree_node
{
	int size;
	bool leaf;
	int counter;
	Vec<Pi<int, int> >data;
	Vec<btree_node*>child;
	btree_node *next;
	btree_node()
	{
		child.resize(order + 1, NULL);
		next = NULL;
		leaf = false;
		size = 0;
		data.resize(order, {inf, inf});
	}
}btree_node;

void fun(int val1, int val2)
{
	//cout << counter << endl;
	int t;
	t=val1;
	val1=val2;
	val2=t;
}

btree_node *root = NULL, *parent = NULL;

btree_node* find(int val)
{
	btree_node *x = root;
	counter++;
	if(x == NULL) 
		return NULL;
	temp++;
	//cout  << val << endl;
	while(x -> leaf != 1)
	{
		int i = 0;
		fun(val,temp);
		while(i < x -> size && val >= x -> data[i].ff)
		{
			counter=temp;
			i++;
			temp++;
		}
		temp--;
		x = x -> child[i];
	}
	return x;
}

int insert_sort(btree_node *x, int val,int _inc)
{
	//cout << _inc << endl;
	_inc++;
	if(x == NULL)
	{
		parent = new btree_node();
		_inc=val;
		root = parent;
		counter++;
		parent = NULL;
		root -> data[root -> size++] = {val, 1};
		//cout << root -> data[root -> size++] << endl;
		return 0;
	}
	if(x -> leaf)
	{
		//cout << "At insert leaf " << endl;
		bool flag = 0;
		counter++;
		fun(counter,_inc);
		for(int i = 0; i < x->size; i++)
		{
			if(x -> data[i].ff == val)
			{
				//cout << "val" << endl;
				fun(x->data[i].ff,_inc);
				x -> data[i].ss++;
				temp++;
				flag = 1;
				break;
			}
		}
		if(flag)
		{
			//cout <<"Not Found" << endl;
			counter--;
			return -1;
		}
	}
	int i = x -> size - 1;
	//cout << counter << endl;
	counter++;
	while(i >= 0 && x -> data[i].ff > val)
	{	
		counter++;
		//cout << val << endl;
		x -> data[i + 1] = x -> data[i];
		fun(val,counter);
		x -> child[i + 2] = x -> child[i + 1];
		counter= val;
		i--;
	}
	x -> data[i + 1] = {val, 1};
	temp = counter;
	x -> size++;
	counter++;
	return i + 1;
}

btree_node* split_node(btree_node *x,int num)
{
	counter++;
	btree_node *tmp = new btree_node();
	int mid = order >> 1;
	if(x -> leaf)
		x->size--;
	else 
		mid++;
	counter++;
	for(int i = mid; i < order; i++)
	{
		counter++;
		tmp -> data[tmp -> size] = x -> data[i];
		temp++;
		tmp -> child[tmp -> size] = x -> child[i];
		//cout << tmp->size;
		x -> size--;
		tmp -> size++;
		//cout << tmp->size;
		counter++;
	}
	tmp -> child[tmp -> size] = x -> child[order];
	counter++;
	if(x -> leaf)
		tmp -> leaf = 1;
	counter++;
	return tmp;
}



void node_balancing(btree_node *r, btree_node *p,int ct)
{
	btree_node *next = r -> next;
	temp++;
	counter++;
	//cout << next->size << endl;
	btree_node *tmp = split_node(r,0);
	counter++;
	//cout << tmp->size << endl;
	int dt = (r -> leaf) ? tmp -> data[0].ff : r -> data[order >> 1].ff;
	temp++;
	//cout << temp <<endl;
	int i = insert_sort(p, dt,temp);
	if(!p) 
		p = root;
	p -> child[i] = r;
	temp=ct;
	//cout << tmp << endl;
	p -> child[i + 1] = tmp;
	p -> leaf = 0;
	if(r -> leaf)
	{
		//cout << tmp -> leaf << endl;
		tmp -> leaf = 1;
		//cout << tmp -> leaf << endl;
		r -> next = tmp;
		temp=1;
		tmp -> next = next;
	}
}

void insertion(btree_node *r, btree_node *p, int val,int t)
{
	counter++;
	//cout << r->size << endl;
	if( !r || r -> leaf)
	{
		//cout << r -> size << endl;
		insert_sort(r, val,counter);
		counter++;
		if(!r) r = root;
		r -> leaf = 1;
	}
	else
	{
		//cout << p->size << endl;
		int i = 0;
		temp++;
		while(val >= r -> data[i].ff) 
		{
			i++;
			counter=i;
		}
		insertion(r -> child[i], r, val,temp);
	}
	if(r -> size == order) 
		node_balancing(r, p,0);
}

void processing(int val1,int val2)
{
	//cout << "Here" << endl;
 	if(!cnt) 
		return;
	//cout << cnt << endl;
	for(int k = 0,ii=0; k < cnt; k++,ii++)
	{
		fun(val1,val2);
		Pi<char, Pi<int, int> > &p = input_buffer[k];
		//cout << input_buffer[k] << endl;

		if(p.ff == 'I') 
		{
			val1++;
			insertion(root, parent, p.ss.ff,0);
			val2++;
		}
		else if(p.ff == 'F')
		{
			//counter++;
			val2++;
			btree_node *x = find(p.ss.ff);
			//cout << x << endl;
			if(!x)
			{
				ii++;
				//cout << "Here" << endl;
				//fun(p.ss.ff,x -> data[0].ff);
				cout << "NO\n";
				temp++;
				counter=ii;
			}
			else
			{
				bool flag = 0,split_flag=1;
				for(int i = 0; i < x -> size; i++)
				{
					split_flag=0;
					//cout << "Yahooooo..." << endl;
					if(p.ss.ff == x -> data[i].ff)
					{
						val1++;
						fun(p.ss.ff,x -> data[i].ff);
						flag = 1;
						val2++;
						cout << "YES\n";
						break;
					}
				}
				if(!flag) 
				{
					//cout << "exit" << endl;
					split_flag=1;
					cout << "NO\n";
				}
			}
		}
		else if(p.ff == 'C')
		{
			btree_node *x = find(p.ss.ff);
			val2++;
			//cout <<" count " << endl;
			if(x == NULL)
			{
				fun(val1,val2);
				cout << "0" << endl;
				continue;
			}
			int flag = 0,split_flag=1;
			val1++;
			for(int i = 0; i < x -> size; i++)
			{
				split_flag=0;
				if(p.ss.ff == x -> data[i].ff)
				{
					fun(p.ss.ff,x->data[i].ff);
					cout << x -> data[i].ss << endl;
					split_flag=1;
					flag = 1;
					//cout << x-> data[i].ss << endl;
					break;
				}
			}
			if(!flag) 
			{
				split_flag=1;
				cout << "0" << endl;
			}
		}
		else if(p.ff == 'R')
		{
			int cnt = 0, flag = 0,split_flag=1;
			temp++;
			btree_node *x = find(p.ss.ff);
			if(x == NULL)
			{
				//cout << "Range" << endl;
				fun(val1,val2);
				cout << "0\n";
				ii++;
				continue;
			}
			while(1)
			{
				int sz = x -> size;
				counter++;
				//cout << counter << endl;
				//cout << sz << endl;
				for(int i = 0; i < sz; i++)
				{
					counter++;
					if(x -> data[i].ff <= p.ss.ss && x -> data[i].ff >= p.ss.ff)
					{ 
						temp++;
						cnt += x -> data[i].ss;
					}
					if(x -> data[i].ff > p.ss.ss)
					{ 
						//cout << val1 << endl;
						//cout << val2 << endl;
						val1=val2;
						flag = 1;
					}
					if(flag)
					{
						//break the loop
						temp++; 
						break;
					}
				}
				//exit condition
				if(flag || x -> next == NULL) 
				{
					temp++;
					//cout << val2 << endl;
					break;
				}
				x = x -> next;
			}
			cout << cnt << endl;
		}
	}
}

int main(int argc, char** argv)
{
	string file, line;
	file = string(argv[1]);
	M = stoi(string(argv[2]));
	B = stoi(string(argv[3]));
	input_buffer.resize(M - 1);
	order = ceil((B - 8) / 12.0);
	ifstream myfile(file);
	while(myfile.is_open())
	{
		cnt = 0;
		input_buffer.clear();
		counter++;
		input_buffer.resize(M - 1);
		temp++;
		while(cnt < M - 1 && (myfile >> line))
		{
			int num1 = -1, num2 = -1;
			temp--;
			myfile >> num1;
			counter++;
			//check for rangr.
			if(line[0] == 'R')
			{
				counter++; 
				myfile >> num2;
			}
			input_buffer[cnt++] = {line[0], {num1, num2}};
			temp--;
		}
		processing(temp,counter);
		if(cnt < M - 1) 
			myfile.close();
		//cout << counter << endl;
		counter=temp;
	}
	return 0;
}