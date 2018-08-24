---
title: 轰炸
date: 2016-10-04 14:49:07
tags: [2016]
categories: daily
ignore: true
---
# 轰炸 ( bomb )
---
- ## [问题]

- ### [问题描述]
> C 国和 W 国爆发了战争!YJC 决定对 W 国的 n 个城市进行轰炸.每个城市都有一个重要度 ai.设 xi=重要度大于 ai的城市数+1,那么第 i 个城市就是第 xi个被轰炸的城市.显然这样能保证重要度大的城市先被轰炸,重要度相同的城市同时被轰炸.现在 YJC 想知道,对于每一个 i,xi等于多少?

<!--more-->

- ### [输入格式]
> 第一行包含一个整数 n,表示城市个数.
> 第二行包含 n 个整数,第 i 个整数 ai表示第 i 个城市的重要度.

- ### [输出格式]
> 一行,包含 n 个整数,第 i 个整数 xi表示第 i 个城市是第几个被轰炸的城市.

- ### [样例]

>> bomb.in | bomb.out
>> --------|---------
>> 5 | 1 3 1 3 3
>> 3 1 3 1 1 |

- ### [数据说明]
> 对于 100%的数据,满足 1≤n≤2000,1≤ai≤109.

- ## [代码]

```c++
#include "stdio.h"
#include "iostream"
#include "algorithm"
using namespace std;

const int N=2004;
const int INF=2147483647;

struct City
{
    int id,ip;
    int x;
}a[N];

int n;

bool operator < (City a,City b)
{
    return a.ip>b.ip;
}

bool operator > (City a,City b)
{
    return a.id<b.id;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("bomb.in","r",stdin);
    freopen("bomb.out","w",stdout);
#endif
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&a[i].ip);
        a[i].id=i;
    }
    sort(a+1,a+1+n,less<City>());
    int cnt=0;
    a[0].ip=-INF;
    for(int i=1;i<=n;i++)
    {
        if(a[i].ip!=a[i-1].ip)
            cnt=i;
        a[i].x=cnt;
    }
    sort(a+1,a+1+n,greater<City>());
    for(int i=1;i<=n;i++)
        printf("%d ",a[i].x);
    return 0;
}
```
