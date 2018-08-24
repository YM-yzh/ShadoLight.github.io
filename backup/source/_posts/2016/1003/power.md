---
title: 幂
date: 2016-10-03 14:36:02
tags: [2016]
categories: daily
ignore: true
---
# 幂 ( power )
---
- ## [问题]

- ### [问题描述]
> YJC 想学习幂级数,但他连幂是什么都不知道.所以他想向你请教:在[L,R]中有多少个数是 n 的整数次幂?

<!--more-->

- ### [输入格式]
> 第一行包含三个整数 L,R 和 n,意思如题所示.

- ### [输出格式]
> 一行,包含一个整数,表示在[L,R]中有多少个数是 n 的整数次幂.

- ### [样例]

>> power.in | power.out
>> ---------|----------
>> 1 10 2 | 4

- ### [数据说明]
> 对于 100%的数据,满足 1≤L≤R≤10<sup>9</sup>,2≤n≤10<sup>9</sup>.

- ## [代码]

```c++
#include "stdio.h"

int l,r,tot;
long long cnt=1,n;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("power.in","r",stdin);
    freopen("power.out","w",stdout);
#endif
    scanf("%d%d%lld",&l,&r,&n);
    while(cnt<l)
        cnt*=n;
    while(cnt<=r)
    {
        tot++;
        cnt*=n;
    }
    printf("%d\n",tot);
    return 0;
}
```
