---
title: 整数拆段
date: 2016-10-01 19:45:23
tags: [2016]
categories: daily
ignore: true
---
# 整数拆段 ( mult )
---
- ## [问题]

- ### [描述]
> 将一个位数为L(4≤L≤10)的自然数N拆成4段,使各段对应的数的乘积最小.你能编一个程序实现吗?

<!--more-->

- ### [输入格式]
> 一个自然数N.

- ### [输出格式]
> 一个整数,最小乘积.

- ### [样例]

>> mult.in | mult.out
>> --------|---------
>> 321457 | 2268

- ### [样例] Explan
> 样例中最小乘积为:3*2*14*27=2268

- ### [数据范围]
> 100%的数据满足:4≤位数L≤10.

- ## [代码]

```c++
#include "stdio.h"
#include "string"
#include "iostream"
using namespace std;

const long long INF=2147483647;

string s;
long long mn=INF;

void DFS(int b,int d,long long tot,long long cnt)
{
    if(b==s.size()+1 and d==5)
    {
        mn=mn<cnt?mn:cnt;
        return ;
    }
    if(b>s.size() or d>4)
        return ;
    tot=tot*10+(s[b-1]-'0');
    DFS(b+1,d,tot,cnt);
    DFS(b+1,d+1,0,tot*cnt);
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("mult.in","r",stdin);
    freopen("mult.out","w",stdout);
#endif
    cin >> s;
    DFS(1,1,0,1);
    cout << mn << endl;
    return 0;
}
```
