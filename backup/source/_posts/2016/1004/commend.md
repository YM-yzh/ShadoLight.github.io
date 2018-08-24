---
title: 表彰
date: 2016-10-04 16:13:11
tags: [2016]
categories: daily
ignore: true
---
# 表彰 ( commend )
---
- ## [问题]

- ### [问题描述]
> 轰炸取得了圆满成功,YJC 决定对飞行员们进行表彰,并选出一名飞行王者.一共有m 名飞行员参加了轰炸,C 国一共有 n 个飞行大队,第 i 个飞行大队认为第 j 个飞行员应该成为飞行王者的人数为 ai,j.对于每一个飞行大队,在这个大队得票最高的飞行员叫做这个大队选择的飞行王者,如果有多个取编号最小的那一个.被最多大队选择的飞行员就是飞行王者,同样如果有多个取编号最小的那一个.现在 YJC 想知道,飞行王者究竟是几号飞行员?

<!--more-->

- ### [输入格式]
> 第一行包含两个整数 n 和 m,表示飞行大队的个数和飞行员的个数.
> 接下来 n 行每行包含 m 个整数,第(i+1)行第 j 个整数 ai,j 表示第 i 个飞行大队认为第 j个飞行员应该成为飞行王者的人数.

- ### [输出格式]
> 一行,包含一个整数,表示飞行王者是几号飞行员.

- ### [样例]

>> commend.in | commend.out
>> -----------|------------
>> 2 2 | 1
>> 2 2 |
>> 1 2 |

- ### [样例解释]
> 在 1 大队,飞行员 1 得到 2 票,飞行员 2 同样得到 2 票,但飞行员 1 编号小,所以 1大队选择飞行员 1 成为飞行王者.
> 在 2 大队,飞行员 1 得到 1 票,飞行员 2 得到 2 票,所以 2 大队选择飞行员 2 成为飞行王者.
> 飞行员 1 被 1 个大队选择,飞行员 2 同样被 1 个大队选择,但飞行员 1 编号小,所以飞行员 1 成为飞行王者.

- ### [数据说明]
> 对于 100%的数据,满足 2≤n,m≤50,0≤ai,j≤109.

- ## [代码]

```c++
#include "stdio.h"
#include "iostream"
#include "algorithm"
using namespace std;

const int N=54;

int n,m;
int a[N][N],bin[N];
int mx,mxi;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("commend.in","r",stdin);
    freopen("commend.out","w",stdout);
#endif
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
    {
        mx=mxi=0;
        for(int j=1;j<=m;j++)
        {
            scanf("%d",&a[i][j]);
            if(a[i][j]>mx)
            {
                mx=a[i][j];
                mxi=j;
            }
        }
        bin[mxi]++;
    }
    mx=mxi=0;
    for(int i=1;i<=n;i++)
    {
        if(bin[i]>mx)
        {
            mx=bin[i];
            mxi=i;
        }
    }
    printf("%d\n",mxi);
    return 0;
}
```
