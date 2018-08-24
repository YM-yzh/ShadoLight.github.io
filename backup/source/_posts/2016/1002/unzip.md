---
title: 解压
date: 2016-10-02 19:23:59
tags: [2016]
categories: daily
ignore: true
---
# 解压 ( unzip )
---
- ## [问题]

- ### [描述]
> 读取一些被压缩的数据,进行解压,再根据题目要求将结果输出至屏幕.

<!--more-->

- ### [输入格式]
> 第一行为一个正整数k,指明以下的数据分为k段.
> 第二行是k段压缩数据串,每个段有两种格式(数之间用一个空格分隔):
> 如果每段第1个数n为正,则该段只有两个数,其解压操作是将该段的第2个数重复n次;
> 如果每段第1个数n为负数,则该段有|n|+1个数,其解压操作是重复该段从第2个数开始的|n|个数一次.(注:|n|表示取n的绝对值)

- ### [输出格式]
> 经解压后得到的整数串上所有数字之和.

- ### [样例]

>> unzip.in | unzip.out
>> ---------|----------
>> 5 | 31
>> 3 2 -5 0 1 2 3 4 5 1 5 0 -4 4 3 2 1

- ### [样例] Explan
> 经解压后得到的整数串 2 2 2 0 1 2 3 4 1 1 1 1 1 0 0 0 0 0 4 3 2 1

- ### [数据范围]
> 100%的数据:k≤10,|n|≤10,其余的数≤10000.

- ## [代码]

```c++
#include "stdio.h"

int t,n,a;
int tot;

int ans(int x)
{
    int cnt=0;
    while(x>0)
    {
        cnt+=x%10;
        x/=10;
    }
    return cnt;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("unzip.in","r",stdin);
    freopen("unzip.out","w",stdout);
#endif
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        if(n>0)
        {
            scanf("%d",&a);
            tot+=ans(a)\*n;
        }
        else
        {
            n=-n;
            for(int i=1;i<=n;i++)
            {
                scanf("%d",&a);
                tot+=ans(a);
            }
        }
    }
    printf("%d\n",tot);
    return 0;
}
```
