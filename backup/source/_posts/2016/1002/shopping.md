---
title: 购物
date: 2016-10-02 20:22:59
tags: [2016]
categories: daily
ignore: true
---
# 购物 ( shopping )
---
- ## [问题]

- ### [描述]
> 今天,金鹰新城市开业了,小Y也去凑热闹.他看到促销广告:商品大减价.于是他很高兴地拿着篮子购物去了.
> 已知商场有n种商品.每种商品的重量为w千克,价格为v,价值为t.此种商品有h件.
>> 注意:此商场有一个奇怪的规定.每种物品要么不买,要么买1件或h件.小Y带了y元且他最多能扛x千克的物品.请帮小Y最多能获得的价值(不允许抢劫).

<!--more-->

- ### [输入格式]
> 第一行有3个用空格隔开的整数n,x和y.
> 接下来的n行,每行有4个数据,分别为w,v,t和h.

- ### [输出格式]
> 仅有一行,表示小Y能获得的最大价值.

- ### [样例]

>> shopping.in | shopping.out
>> ------------|-------------
>> 2 8 10 | 17
>> 5 3 7 1
>> 3 7 10 1

- ### [数据范围]
> 100%的数据满足:0≤n≤300,0≤x≤100,0≤y≤100,0≤h≤10.

- ## [代码]

```c++
#include "stdio.h"

const int N=304;

struct Item
{
    int w,v,t,h;
}a[N];

int n,W,V;
int f[N][N];

inline int mx(int x,int y)
{
    return x>y?x:y;
}

int Choose(int i,int j,int k)
{
    int x=f[j-a[i].w][k-a[i].v]+a[i].t;
    int y=0;
    if(j>=a[i].w*a[i].h and k>=a[i].v*a[i].h)
        y=f[j-a[i].w*a[i].h][k-a[i].v*a[i].h]+a[i].t*a[i].h;
    return mx(x,y);
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("shopping.in","r",stdin);
    freopen("shopping.out","w",stdout);
#endif
    scanf("%d%d%d",&n,&W,&V);
    for(int i=1;i<=n;i++)
        scanf("%d%d%d%d",&a[i].w,&a[i].v,&a[i].t,&a[i].h);
    for(int i=1;i<=n;i++)
        for(int j=W;j>=a[i].w;j--)
            for(int k=V;k>=a[i].v;k--)
            {
                f[j][k]=mx(f[j][k],Choose(i,j,k));
            }
    printf("%d\n",f[W][V]);
    return 0;
}
```
