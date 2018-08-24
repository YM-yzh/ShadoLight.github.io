---
title: 苟
date: 2016-10-02 16:15:57
tags: [2016]
categories: daily
ignore: true
---
# 苟 ( gou )
---
- ## [问题]

- ### [问题描述]
> 苟先生有一个字符串,不过他的朋友富先生对他的字符串做了一些小手脚,不仅打乱了顺序而且还把一些字符变成了*,而且这个字符串混进了一大堆字符串中,苟先生想知道哪些可能是他的字符串.

<!--more-->

- ### [输入格式]
> 第一行一个整数 n 表示字符串长度.
> 第二行一个只含小写字母的长度为 n 的字符串表示苟先生的串.
> 第三行一个整数 m 表示混进的字符串数量.
> 接下来 m 行每行一个长度为 n 的字符串,包含小写字母和*.

- ### [输出格式]
> 输出一行一个 m 位的二进制数,如果第 i 个字符串可能是苟先生的,第 i位就为 1,否则为 0.

- ### [样例]

>> gou.in | gou.out
>> -------|--------
>> 3 | 101
>> aba |
>> 3 |
>> aab |
>> bb* |
>> a** |

- ### [数据范围]
> 对于 40%的数据不含*;
> 对于 100%的数据 n,m≤100.

- ## [代码]

```c++
#include "stdio.h"
#include "iostream"
#include "algorithm"
using namespace std;

const int N=104;

int n,m;
char org[N],str[N];
int cnt;

bool cmp(char a,char b)
{
    if (a=='*')
        return false;
    if (b=='*')
        return true;
    return a < b;
}

bool op(const char *a,const char *b)
{
    int i,j;
    for(i=0,j=0;i<n;i++)
    {
        if(a[i]!=b[j])
        {
            if(cnt)
            {
                cnt--;
                continue;
            }
            else
                return false;
        }
        j++;
    }
    return true;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("gou.in", "r", stdin);
    freopen("gou.out", "w", stdout);
#endif
    scanf("%d",&n);
    scanf("%s",org);
    sort(org,org+n,cmp);
    scanf("%d",&m);
    for(int i=1;i<=m;i++)
    {
        cnt=0;
        scanf("%s",str);
        sort(str,str+n,cmp);
        for(int k=0;k<n;k++)
            if(str[k]=='*')
                cnt++;
        if (op(org,str))
            printf("1");
        else
            printf("0");
    }
    return 0;
}
```
