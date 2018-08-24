---
title: 赌徒
date: 2016-10-02 22:05:47
tags: [2016]
categories: daily
ignore: true
---
# 赌徒 ( gambler )
---
- ## [问题]

- ### [描述]
> 有N个赌徒,手里各自有自己的筹码.在赌博时,他们能向周围的赌徒借钱,所以他们的筹码可能是负的,但筹码都一定是整数.当结束赌博时,N个赌徒当中,筹码刚是另外3个人筹码的总和的赌徒为胜者.如果有多个符合条件的赌徒,选择筹码最大的那个人为胜者.例如 5个赌徒,结束赌博时各有 2,3,5,7,12,则他们中的胜者是持有12的人,因为 12=2+3+7.

<!--more-->

- ### [输入格式]
> 第一行为一个整数n,表示有n个赌徒.接下去n行,每行一个整数x表示赌博结束时,每个赌徒手中的筹码.

- ### [输出格式]
> 仅一个整数表示赌博结束时,胜者手中的筹码数.如果没有胜者则输出“no solution”.

- ### [样例]

>> gambler.in | gambler.out
>> -----------|------------
>> 5 | 12
>> 2
>> 3
>> 5
>> 7
>> 12

- ### [数据范围]
> 50%的数据满足:1≤n≤100;
> 100%的数据满足:1≤n≤1000,-10^8≤x≤10^8.

- ## [代码]

```c++
#include "stdio.h"
#include "algorithm"
using namespace std;

const int N=1004;
const int MOD=4544443;

struct List
{
    int s;
    int a,b;
    int n;
}l[N*N];

int n,li;
int a[N],tot[MOD];

inline int ab(int x)
{
    return x<0?-x:x;
}

void add(int a,int b,int s)
{
    l[++li].s=s;l[li].a=a;l[li].b=b;
    l[li].n=tot[ab(s)%MOD];
    tot[ab(s)%MOD]=li;
}

bool op(int a,int b,int s)
{
    for(int i=tot[ab(s)%MOD];i>=1;i=l[i].n)
        if(l[i].s==s and l[i].a!=a and l[i].b!=b and l[i].a!=b and l[i].b!=a)
            return true;
    return false;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("gambler.in","r",stdin);
    freopen("gambler.out","w",stdout);
#endif
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    sort(a+1,a+1+n);
    for(int i=1;i<=n;i++)
        for(int j=i+1;j<=n;j++)
            add(i,j,a[i]+a[j]);
    bool f=false;
    for(int i=n;i>=1;i--)
    {
        for(int j=1;j<=n;j++)
            if(i!=j and op(i,j,a[i]-a[j]))
            {
                printf("%d\n",a[i]);
                f=true;
                break;
            }
        if(f)
            break;
    }
    if(!f)
        puts("no solution");
    return 0;
}
```
