---
title: 编号
date: 2016-10-01 19:44:25
tags: [2016, 洛谷]
categories: daily
ignore: true
---
# 编号 ( number )
---
- ## [来源]
- @[洛谷 P1866](https://www.luogu.org/problem/show?pid=1866)

- ## [问题]

- ### [描述]
> 太郎有N只兔子,现在为了方便识别它们,太郎要给他们编号.兔子们向太郎表达了它们对号码的喜好,每个兔子i想要一个整数,介于1和MaxNumber[i]之间(包括1和MaxNumber[i]).当然,每个兔子的编号是不同的.现在太郎想知道一共有多少种编号的方法.
> 你只用输出答案mod 1000000007即可.如果这是不可能的,就输出0.

<!--more-->

- ### [输入格式]
> 第一行是一个整数N(1≤N≤50).
> 第二行N个整数MaxNumber[i] (1≤MaxNumber[i]≤1000).

- ### [输出格式]
> 一个整数 ,表示方案总数 mod 1000000007的值.

- ### [样例]

>> number.in | number.out
>> ----------|-----------
>> 2 | 35
>> 5 8

- ### [数据范围]
> 100%的数据:1≤N≤50,1≤MaxNumber[i]≤1000.

- ## [代码]

```c++
#include "stdio.h"
#include "algorithm"
using namespace std;

const int N=54;
const int MOD=1000000007;

int n;
long long a[N];
long long tot=1;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("number.in","r",stdin);
    freopen("number.out","w",stdout);
#endif
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    sort(a+1,a+1+n);
    for(int i=1;i<=n;i++)
    {
        tot*=a[i]-i+1;
        tot%=MOD;
    }
    printf("%d\n",tot);
    return 0;
}
```
