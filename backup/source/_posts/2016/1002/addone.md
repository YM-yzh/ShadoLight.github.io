---
title: 加一
date: 2016-10-02 17:03:25
tags: [2016]
categories: daily
ignore: true
---
# 加一 ( addone )
---
- ## [问题]

- ### [问题描述]
> 你的任务是很简单,给你一个非负整数 N,输出 N+1.
> 唯一的复杂之处在于给出的整数是一个 2~36 进制(包括边界)中一个未知进制的整数.(大家知道的,从 10 开始的数字分别用 A,B,C,……来表示)因此,你的程序必须按字典序递增输出所有可能的结果.

<!--more-->

- ### [输入格式]
> 一行,包含一个由数字 0 至 9 与大写字母 A 至 Z 组成的整数 N,数据保证没有前导零.

- ### [输出格式]
> 输出所有的可能结果,每个结果占一行.

- ### [样例]

>> addone1.in | addone1.out
>> ----------|-----------
>> 32 | 33

>> addone2.in | addone2.out
>> ----------|-----------
>> 9 | 10
>>  | A

- ### [样例 2 说明]
> 9 是 10 进制则加 1 答案为 10,为大于 10 进制时则加 1 答案为 A.

- ### [数据范围]
> N 包含 1 至 200 位数字.

- ## [代码]

```c++
#include "stdio.h"

int n;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("addone.in","r",stdin);
	freopen("addone.out","w",stdout);
#endif
	scanf("%d",&n);
	printf("%d\n",n+1);
	return 0;
}
```
