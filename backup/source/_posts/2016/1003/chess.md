---
title: 国际象棋
date: 2016-10-03 16:10:59
tags: [2016]
categories: daily
ignore: true
---
# 国际象棋 ( chess )
---
- ## [问题]

- ### [问题描述]
> YJC 想学习国际象棋,但他连个子怎么走都不会.所以他决定练习怎么走子.
> YJC 有一块 n*m 的棋盘,他在上面摆了若干个皇后,皇后可以走到同一行,同一列,同一条对角线上的任意一个格子.现在他想知道:有多少个格子满足上面有皇后或者可以被某个皇后走到?

<!--more-->

- ### [输入格式]
> 第一行包含两个整数 n 和 m,表示棋盘的行数和列数.
> 接下来 n 行每行包含 m 个字符,第(i+1)行第 j 个字符如果是'.'表示上面没有放皇后,如果是'X'表示上面放了皇后.

- ### [输出格式]
> 一行,包含一个整数,表示有多少个格子满足上面有皇后或者可以被某个皇后走到.

- ### [样例]

>> chess.in | chess.out
>> ---------|----------
>> 2 2 | 4
>> .X |
>> X. |

- ### [数据说明]
> 对于 100%的数据,满足 2≤n,m≤50.

- ## [代码]

```c++
#include "stdio.h"

const int N=54;

int n,m;
bool map[N][N];
int tot;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("chess.in","r",stdin);
    freopen("chess.out","w",stdout);
#endif
    scanf("%d%d\n",&n,&m);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            char c=getchar();
            if(c=='X')
            {
                for(int jj=1;jj<=m;jj++)
                    map[i][jj]=true;
                for(int ii=1;ii<=n;ii++)
                    map[ii][j]=true;
                for(int ii=i,jj=j;ii>=1 and jj>=1;ii--,jj--)
                    map[ii][jj]=true;
                for(int ii=i,jj=j;ii<=n and jj<=m;ii++,jj++)
                    map[ii][jj]=true;
                for(int ii=i,jj=j;ii>=1 and jj<=m;ii--,jj++)
                    map[ii][jj]=true;
                for(int ii=i,jj=j;ii<=n and jj>=1;ii++,jj--)
                    map[ii][jj]=true;
            }
        }
        getchar();
    }
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            tot+=map[i][j];
    printf("%d\n",tot);
    return 0;
}
```
