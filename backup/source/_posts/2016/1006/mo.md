---
title: 魔
date: 2016-10-06 16:39:38
tags: [2016]
categories: daily
ignore: true
---
# 魔 ( mo )
---
- ## [问题]

- ### [问题描述]
> 有 n 个恶魔降临了...小 S 决定打击这些恶魔,她的魔法能在一瞬间同时杀死任意数量的恶魔,但是有些恶魔之间存在保护关系,比如恶魔 A 保护恶魔 B,则如果 A 不死则 B 不受伤害,现在小 S 想知道最少需要使用多少次魔法才能杀死所有恶魔,如果不能杀死所有恶魔,输出-1.

<!--more-->

- ### [输入格式]
> 第一行两个个正整数 n 和 m 分别表示恶魔数和保护关系对数.接下来 m 行每行两个数 A 和 B 描述一对保护关系.

- ### [输出格式]
> 一行一个整数表示答案.

- ### [样例]

>> mo.in | mo.out
>> ------|-------
>> 3 2 | 2
>> 1 2 |
>> 3 2 |

- ### [数据范围]
> 20%的数据:n≤10;
> 40%的数据:n≤100;
> 60%的数据:n≤1000;
> 80%的数据:n≤10000;
> 100%的数据:n≤100000.

- ## [代码]
```c++
#include "stdio.h"
#include "deque"
using namespace std;

const int N=1e+5 +4;

struct Demon
{
	int id;
	int no;
};

int n,m;
int De[N];
int ans;

int ft[N],nt[N],ed[N];
bool vis[N];

void add(int u,int v,int TNT)
{
	nt[TNT]=ft[u];
	ft[u]=TNT;
	ed[TNT]=v;
}

bool topo()
{
	deque<Demon> q;
	for(int i=1;i<=n;i++)
		if(De[i]==0)
			q.push_back((Demon){i,1});
	int tot=0;
	while(q.size())
	{
		Demon t=q.front();
		ans=t.no;
		tot++;
		q.pop_front();
		for(int i=ft[t.id];i;i=nt[i])
		{
			De[ed[i]]--;
			if(De[ed[i]]==0)
				q.push_back((Demon){ed[i],t.no+1});
		}
	}
	return tot<n;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("mo.in","r",stdin);
	freopen("mo.out","w",stdout);
#endif
	scanf("%d%d",&n,&m);
	for(int i=1,a,b;i<=m;i++)
	{
		scanf("%d%d",&a,&b);
		add(a,b,i);
		De[b]++;
	}
	if(topo())
		return puts("-1") and false;
	return printf("%d\n",ans) and false;
}
```
