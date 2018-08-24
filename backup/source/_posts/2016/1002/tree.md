---
title: 构建二叉树
date: 2016-10-02 15:26:23
tags: [2016]
categories: daily
ignore: true
---
# 构建二叉树 ( tree )
---
- ## [问题]

- ### [问题描述]
> 树的表示方法很多,可以采用自然界的树形表示法如图,另外也可以采用括号表示法,先将根结点放入一对圆括号中,然后把它的子树按由左往右的顺序放入括号中,而对子树也采用同样的方法处理.同层子树与它的根结点用圆括号扩起来,同层子树之间用逗号格开,最后用闭括号括起来.如图所示的树可以表示成:
> (1(2(4,5),3))
> 由完全二叉树的定义我们可知,如果知道该完全二叉树的结点个数,则可以构建出一棵确定的完全二叉树,现在输入完全二叉树的结点数 N(N≤2 <sup>14</sup> ), 用括号表示法输出这棵树.(默认树的结点名称为树结点的编号)

<!--more-->

- ### [输入格式]
> N 完全二叉树的结点个数.

- ### [输出格式]
> N 个结点的完全二叉树的括号表示.

- ### [样例]

>> tree.in | tree.out
>> --------|---------
>> 5 | (1(2(4,5),3))

- ## [代码]

```c++
#include "stdio.h"

int n;

void DFS(int i)
{
    if(i>n)
        return ;
    printf("%d",i);
    if(i*2<=n)
    {
        printf("(");
        if(i*2<=n)
            DFS(i*2);
        if(i*2+1<=n)
        {
            printf(",");
            DFS(i*2+1);
        }
        printf(")");
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("tree.in","r",stdin);
    freopen("tree.out","w",stdout);
#endif
    scanf("%d",&n);
    printf("(");
    DFS(1);
    printf(")");
    return 0;
}
```
