---
title: 传球游戏
date: 2016-10-02 10:48:59
tags: [2016]
categories: daily
ignore: true
---
# 传球游戏 ( passball )
---
- ## [问题]

- ### [题目描述]:
> 上体育课的时候,小蛮的老师经常带着同学们一起做游戏.这次,老师带着同学们一起做传球游戏.
> 游戏规则是这样的:n个同学站成一个圆圈,其中的一个同学手里拿着一个球,当老师吹哨子时开始传球,每个同学可以把球传自己左右的两个同学中的一个(左右任意),当老师再次吹哨子时,传球停止,此时,拿着球没传出去的那个同学就是败者,要大家表演一个节目.
> 聪明的小蛮提出了一个有趣的问题:有多少种不同的传球方法可以使得从小蛮手里开始传的球,传了m次以后,又回到小蛮手里两种传球方法被视作不同的方法,当且仅当这两种方法中,接到球的同学按接球顺序组成的序列是不同的.比如有三个同学1号,号,3号,并假设小蛮为1号,球传了三次回到小蛮手里的方式有1->2->3->1和1->3->2->1,共2种.

<!--more-->

- ### [输入描述]:
> 输入共一行,有两个用空格隔开的整数n,m(3<=n<=30,1<=m<=30).

- ### [输出描述]:
> 输出共一行,有一个整数,标示符合题意的方法数.

- ### [样例]

>> passball.in | passball.out
>> ------------|-------------
>> 3 3 | 2

- ## [代码]

```c++
#include "stdio.h"
#include "string.h"
#include "iostream"
using namespace std;

const int N=34;

int n,m;
int f[N][N];

int DFS(int i,int s)
{
    if(s==0)
    {
        if(i==1)
            return 1;
        return 0;
    }
    if( not (f[i][s]==-1))
        return f[i][s];
    return f[i][s]=DFS(i==n?1:i+1,s-1)+DFS(i==1?n:i-1,s-1);
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("passball.in","r",stdin);
    freopen("passball.out","w",stdout);
#endif
    memset(f,-1,sizeof(f));
    cin >> n >> m;
    cout << DFS(1,m);
    return 0;
}
```
