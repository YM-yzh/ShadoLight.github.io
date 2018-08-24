---
title: 序列
date: 2016-10-03 20:31:48
tags: [2016]
categories: daily
ignore: true
---
# 序列 ( seq )
---
- ## [问题]

- ### [描述]
> 我们按以下方式产生序列:
> 1, 开始时序列是: "O" ;
> 2, 每一次变化把序列中的 "O" 变成 "OI" ,"I" 变成 "O".
> 经过无限次变化,我们得到序列"OIOOIOIOOIOOIOIOOIO....".
> 总共有 Q个询问,每次询问为:在区间[a,b]之间有多少个"O".
> 请写一个程序回答Q个询问

<!--more-->

- ### [输入格式]
> 第一行为一个整数Q;
> 接下来有Q行,每行两个数用空格隔开的整数a, b.

- ### [输出格式]
> 共Q行,每行一个回答.

- ### [样例]

>> seq.in | seq.out
>> -------|--------
>> 1 | 4
>> 2 8

- ### [数据范围]
> 100%的数据: 1≤Q≤5000,1≤a≤b<2^63.

- ## [代码]

```c++
#include "stdio.h"

const int N=92;

int n;
long long x[N+4],y[N+4];

long long find(long long a)
{
    int i;
    for(i=1;i<=N;i++)
        if(x[i]>=a)
            break;
    if(a==x[i])
        return y[i];
    return y[i-1]+find(a-x[i-1]);
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("seq.in","r",stdin);
    freopen("seq.out","w",stdout);
#endif
    x[1]=1;x[2]=2;
    y[1]=y[2]=1;
    for(int i=3;i<=N;i++)
    {
        x[i]=x[i-1]+x[i-2];
        y[i]=y[i-1]+y[i-2];
    }
    scanf("%d",&n);
    while(n--)
    {
        long long a,b;
        scanf("%lld%lld",&a,&b);
        long long ans=find(b)-find(a-1);
        printf("%lld\n",ans);
    }
    return 0;
}
```
