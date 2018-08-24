---
title: 矩阵相似
date: 2016-10-02 14:42:41
tags: [2016]
categories: daily
ignore: true
---
# 矩阵相似 ( matrix )
---
- ## [问题]

- ### [问题描述]
> 给出 2 个大小相同的矩阵方阵 A,B,方阵中的元素为 0 或 1.若 A 和 B相似,满足下面条件:
> >* A=B --> 输出 0
> >* A 经过顺时针旋转 90°成为 B --> 输出 1
> >* A 经过顺时针旋转 180°成为 B --> 输出 2
> >* A 经过顺时针旋转 270°成为 B --> 输出 3
> >* 若 A,B 不相似 --> 输出-1

<!--more-->

- ### [输入格式]
> 第一行为一个整数 n;
> 接下来的 n 行表示 A 矩阵的 01 方阵;
> 再接下来的 n 行表示 B 矩阵的 01 方阵.

- ### [输出格式]
> 一个整数(0,或 1,或 2, 或 3,或-1)即 A,B 相似的结果.

- ### [样例]

>> matrix.in | matrix.out
>> ----------|-----------
>> 4 | 1
>> 0 0 0 0 |
>> 0 0 0 0 |
>> 0 1 0 0 |
>> 0 0 0 0 |
>> 0 0 0 0 |
>> 0 1 0 0 |
>> 0 0 0 0 |
>> 0 0 0 0 |

- ### [数据范围]
> 100%的数据:1≤n≤20

- ## [代码]

```c++
#include "stdio.h"

const int N=24;

int n;
int A,B,C,R;
bool a[N][N],b[N][N];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("matrix.in","r",stdin);
    freopen("matrix.out","w",stdout);
#endif
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            scanf("%d",&a[i][j]);
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            scanf("%d",&b[i][j]);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            A+=(a[i][j]==b[j][n+1-i]);
            B+=(a[i][j]==b[n+1-i][n+1-j]);
            C+=(a[i][j]==b[n+1-j][i]);
            R+=(a[i][j]==b[i][j]);
        }
    }
    if(R==n*n)
        puts("0");
    else if(A==n*n)
        puts("1");
    else if(B==n*n)
        puts("2");
    else if(C==n*n)
        puts("3");
    else
        puts("-1");
    return 0;
}
```
