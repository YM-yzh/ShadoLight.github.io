---
title: 回文串
date: 2016-10-05 13:07:37
tags: [2016]
categories: daily
ignore: true
---
# 回文串 ( palind )
---
- ## [问题]

- ### [问题描述]
> 输入一个只由大小写字母,数字组成的字符串,计算至少添加几个字符才能使得它变成一个回文串.

<!--more-->

- ### [输入格式]
> 第一行为正整数t(≤5),表示数据组数;接下来t行,每行一个只由大小写字母和数字组成的字符串,长度不超过5000.

- ### [输出格式]
> 对于每组数据,输出最少添加字符数.

- ### [样例]

>> palind.in | palind.out
>> ----------|-----------
>> 2 | 2
>> Ab3bd | 2
>> abcdcda |

- ## [代码]

```c++
#include "stdio.h"
#include "string.h"
#include "algorithm"
using namespace std;

const int N=5004;

int t,n;
char a[N],b[N];
int f[N][N];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("palind.in","r",stdin);
	freopen("palind.out","w",stdout);
#endif
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",a);
		n=strlen(a);
		for(int i=1;i<=n;i++)
		{
			f[i][0]=0;
			b[n-i]=a[i-1];
		}
		for(int i=1;i<=n;i++)
			f[0][i]=0;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
			{
				if(a[i-1]==b[j-1])
					f[i][j]=f[i-1][j-1]+1;
				else
					f[i][j]=max(f[i-1][j],f[i][j-1]);
			}
		printf("%d\n",n-f[n][n]);
	}
	return 0;
}
```
