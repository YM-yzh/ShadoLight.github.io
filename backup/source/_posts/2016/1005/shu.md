---
title: 数
date: 2016-10-05 17:21:27
tags: [2016]
categories: daily
ignore: true
---
# 数 ( shu )
---
- ## [问题]

- ### [问题描述]
> 将 N 个整数排成一行,每个整数 a[i]的值在(-10000 ≤ a[i] ≤10000).然后从这一行数中进行取数,其规则是:可从这一行中的任何一个位置开始取数,到任何位置结束,但不能不取.找出一种取法,使得取得的和为最大,再找出一种取法,使得取得的和为最小.例如: N=4, 4 个数依次为:13,-6,7,-8 取得和为最大的是:13+(-6)+7=14 取得和为最小的是:-8.

<!--more-->

- ### [输入格式]
> 第一行有一个整数 N,第二行为 N 个整数.

- ### [输出格式]
> 输出二行,第一行一个整数表示取得和的最大值,第二行一个整数表示取得和的最小值.

- ### [样例]

>> shu.in | shu.out
>> -------|--------
>> 4 | 14
>> 13 -6 7 -8 | -8

- ## [代码]

```c++
#include "stdio.h"

const int INF=2147483647;

int n;
int mx=-INF,mn=+INF;
int mxs,mns;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("shu.in","r",stdin);
    freopen("shu.out","w",stdout);
#endif
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        int a;
        scanf("%d",&a);
        mxs=mxs+a<0?0:mxs+a;
        mns=mns+a>0?0:mns+a;
        mx=mx>mxs?mx:mxs;
        mn=mn<mns?mn:mns;
    }
    printf("%d\n%d\n",mx,mn);
    return 0;
}
```
