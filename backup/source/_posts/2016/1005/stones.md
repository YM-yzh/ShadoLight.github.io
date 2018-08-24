---
title: 石子合并
date: 2016-10-05 12:59:29
tags: [2016]
categories: daily
ignore: true
---
# 石子合并 ( stones )
---
- ## [问题]

- ### [问题描述]
> 有N(≤200)堆石子排成一排,每堆石子有一定的数量.现要将N堆石子合并成为一堆.合并的过程只能每次将相邻的两堆石子堆成一堆,每次合并花费的代价为这两堆石子的和,经过N-1次合并后成为一堆.求出总的代价最小值.

<!--more-->

- ### [输入格式]
> 第一行为正整数t(≤5),表示数据组数;每组数据中,第一行为正整数n(≤200),表示石子总数,第二行为以空格隔开的n个正整数ai(≤1000),分别表示每堆石子的个数.

- ### [输出格式]
> 对于每组数据,输出最小总代价.

- ### [样例]

>> stones.in | stones.out
>> ----------|-----------
>> 2 | 9
>> 3 | 239
>> 1 2 3 |
>> 7 |
>> 13 7 8 16 21 4 18 |

- ## [代码]

```c++
#include "stdio.h"
#include "string.h"
#include "iostream"
using namespace std;

const int N=204;
const int INF=2147483647;

int t,n;
int a[N],s[N];
int f[N][N];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("stones.in","r",stdin);
	freopen("stones.out","w",stdout);
#endif
	scanf("%d",&t);
	while(t--)
	{
		cin >> n;
		for(int i=1;i<=n;i++)
		{
			cin >> a[i];
			s[i]=s[i-1]+a[i];
		}
		memset(f,0,sizeof(f));
		for(int l=2;l<=n;l++)
		{
			for(int i=1;i<=n-l+1;i++)
			{
				int j=i+l-1;
				f[i][j]=INF;
				for(int k=i;k<j;k++)
					f[i][j]=min(f[i][j],f[i][k]+f[k+1][j]+s[j]-s[i-1]);
			}
		}
		cout << f[1][n] << endl;
	}
	return 0;
}
```
