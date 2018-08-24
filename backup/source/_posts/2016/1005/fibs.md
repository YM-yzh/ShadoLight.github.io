---
title: Fib之奇偶性
date: 2016-10-05 12:47:19
tags: [2016]
categories: daily
ignore: true
---
# Fib之奇偶性 ( fibs )
---
- ## [问题]

- ### [问题描述]
> Fibonacci数列大家都已经很熟悉了:f(0)=0,f(1)=1, f(n)=f(n-1)+f(n-2) n≥2.给定正整数n,判别数列第n项的奇偶性.

<!--more-->

- ### [输入格式]
> 第一行为正整数t(≤100),表示数据组数;接下来t行,每行一个正整数n(≤108).

- ### [输出格式]
> 输出第n项Fibonacci数列的奇偶性,如果为奇数则请输出“ODD”,否则为“EVEN”.

- ### [样例]

>> fibs.in | fibs.out
>> --------|--------
>> 3 | ODD
>> 1 | ODD
>> 2 | EVEN
>> 3 |

- ## [代码]

```c++
#include "stdio.h"

int t,n;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("fibs.in","r",stdin);
	freopen("fibs.out","w",stdout);
#endif
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		n%=3;
		if(!n)
			puts("EVEN");
		else
			puts("ODD");
	}
	return 0;
}
```
