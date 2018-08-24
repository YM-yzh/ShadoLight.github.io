---
title: 冰雹序列
date: 2016-10-02 11:37:27
tags: [2016]
categories: daily
ignore: true
---
# 冰雹序列 ( hailstone )
---
- ## [问题]

- ### [题目描述]:
> 冰雹序列是这样形成的:
> 1,如果N为偶数,则将其除以2;
> 2,如果N为奇数,则将其乘以3在加上1;
> 这个序列最后总是在:4 2 1 循环.所以当N==1,时我们认为序列结束.
> 写一个程序,计算出序列中的最大值.

<!--more-->

- ### [输入描述]:
> 第一行给出P(1<= P <= 100,000)表示测试组数.
> 每组数据一行两个整数:第一个是测试组数;
> 第二个数是N (1 <=  n  <=  100,000),表示序列起始值;

- ### [输出描述]:
> 输出每组测试一行两个整数.第一个数是测试组数;
> 第二个数是这是序列的最大值(不超过int类型).


- ### [样例]

>> hailstone.in | hailstone.out
>> -------------|--------------
>> 4 | 1 1
>> 1 1 | 2 16
>> 2 3 | 3 101248
>> 3 9999 | 4 100000
>> 4 100000

- ## [代码]

```c++
#include "stdio.h"

const int N=40000004;

int t,n;
int f[N];

int mx(int a,int b)
{
    return a>b?a:b;
}

int DFS(int x)
{
    if(x>N)
    {
        switch(x&1)
        {
            case 0:return mx(x,DFS(x/2));
            case 1:return mx(x*3+1,DFS(x*3+1));
        }
    }
    if(f[x])
        return f[x];
    if(x==1)
        return 1;
    switch(x&1)
    {
        case 0:f[x]=mx(x,DFS(x/2));break;
        case 1:f[x]=mx(x*3+1,DFS(x*3+1));break;
    }
    return f[x];
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("hailstone.in","r",stdin);
    freopen("hailstone.out","w",stdout);
#endif
    scanf("%d",&t);
    for(int ti=1;ti<=t;ti++)
    {
        scanf("%\*d%d",&n);
        printf("%d %d\n",ti,DFS(n));
    }
    return 0;
}

```
