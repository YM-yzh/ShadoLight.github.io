---
title: 生产调度
date: 2016-10-01 19:45:25
tags: [2016 ,洛谷, Code VS]
categories: daily
ignore: true
---
# 生产调度 ( dispatch )
---
- ## [来源]
- ~~@[洛谷 P1248](https://www.luogu.org/problem/show?pid=1248)~~
- @[Code VS 3008](http://codevs.cn/problem/3008/)
- @[TYVJ P3016](http://tyvj.cn/p/3016)

- ## [问题]

- ### [描述]
> 某工厂收到了n个产品的订单,这n个产品分别在A,B两个车间加工,并且必须先在A车间加工后才可以到B车间加工.
> 某个产品i在A,B两车间加工的时间分别为Ai,Bi.怎样安排这n个产品的加工顺序,才能使总的加工时间最短.这里所说的加工时间是指:从开始加工第一个产品到最后所有的产品都已在A,B两车间加工完毕的时间.

<!--more-->

- ### [输入格式]
> 第一行仅—个数据n,表示产品的数量.
> 接下来n个数据是表示这n个产品在A车间加工各自所要的时间(都是整数).
> 最后的n个数据是表示这n个产品在B车间加工各自所要的时间(都是整数).

- ### [输出格式]
> 第一行一个数据,表示最少的加工时间;

- ### [样例]

>> dispatch.in | dispatch.out
>> ------------|-------------
>> 5 | 34
>> 3 5 8 7 10 |
>> 6 2 1 4 9 |

- ### [数据范围]
> 100%的数据:1≤n≤1000.

- ## [代码]

```c++
#include "stdio.h"
#include "algorithm"
using namespace std;

const int N=1004;

struct Node
{
    int x,id;
}m[N];

int n;
int a[N],b[N],f[N];

bool cmp(const Node&a,const Node&b)
{
    return a.x<b.x;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("dispatch.in","r",stdin);
    freopen("dispatch.out","w",stdout);
#endif
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    for(int i=1;i<=n;i++)
        scanf("%d",&b[i]);
    for(int i=1;i<=n;i++)
        m[i]=(Node){min(a[i],b[i]),i};
    sort(m+1,m+1+n,cmp);
    int p1=1,pn=n;
    for(int i=1;i<=n;i++)
        if(m[i].x==a[m[i].id])
            f[p1++]=m[i].id;
        else
            f[pn--]=m[i].id;
    int sa=0,sb=0;
    for(int i=1;i<=n;i++)
    {
        sa+=a[f[i]];
        sb=max(sa,sb)+b[f[i]];
    }
    printf("%d\n",sb);
    return 0;
}
```
