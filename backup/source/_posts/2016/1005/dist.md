---
title: 编辑距离
date: 2016-10-05 12:56:43
tags: [2016]
categories: daily
ignore: true
---
# 编辑距离 ( dist )
---
- ## [问题]

- ### [问题描述]
> 编辑距离是指两个字串之间,由一个转成另一个所需的最少编辑操作次数,允许的编辑操作包括:将一个字符替换成另一个字符,插入一个字符,删除一个字符.给出两个字符串s1和s2,找出它们之间的编辑距离,即由字符串s1最少经过多少步操作变成字符串s2.

<!--more-->

- ### [输入格式]
> 两行字符串,全部由小写字母组成,长度均不超过1000.

- ### [输出格式]
> 只包含一个整数,表示两个字符串的编辑距离.

- ### [样例]

>> dist.in | dist.out
>> --------|--------
>> abcde | 4
>> acefg |

- ## [代码]

```c++
#include "stdio.h"
#include "string"
#include "iostream"
using namespace std;

const int N=1004;

string a,b;
int f[N][N];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("dist.in","r",stdin);
	freopen("dist.out","w",stdout);
#endif
	cin >> a >> b;
	for(int i=1;a[i-1];i++)
		f[i][0]=i;
	for(int i=1;b[i-1];i++)
		f[0][i]=i;
	for(int i=1;a[i-1];i++)
		for(int j=1;b[j-1];j++)
		{
			int c=1;
			if(a[i-1]==b[j-1])
				c=0;
			f[i][j]=min(f[i-1][j]+1,min(f[i][j-1]+1,f[i-1][j-1]+c));
		}
	printf("%d\n",f[a.size()][b.size()]);
	return 0;
}
```
