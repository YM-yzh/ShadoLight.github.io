---
title: 密码解压
date: 2016-10-01 19:44:25
tags: [2016]
categories: daily
ignore: true
---
# 密码解压 ( password )
---
- ## [问题]

- ### [描述]
> 为了保护日益恶劣的地球环境,地球防卫小队决定去求助外星种族的帮助.经过很长时间的努力,小队终于收到了外星生命的回信.但是外星人发过来的却是一串密码.只有解开密码,才能知道外星人给的准确回复.解开密码的第一道工序就是解压缩密码,外星人对于连续的若干个相同的子串“x”会压缩为“[DX]”的形式(D是一个整数且1≤D≤99),比如说字符串“CBCBCBCB”就压缩为“[4CB]”或者“[2[2CB]]”,类似于后面这种压缩之后再压缩的我们称之为二重压缩.如果是“[2[2[2CB]]]",则是三重.
> 现在我们给你外星人发送的密码,请你对其进行解压缩.

<!--more-->

- ### [输入格式]
> 一行,包含一个字符串, 输入只包含数字,大写字母, "[" 和 "]" .

- ### [输出格式]
> 一行,即一个解压缩后的字符串.

- ### [样例]

>> password.in | password.out
>> ------------|-------------
>> AC[3FUN] | ACFUNFUNFUN

- ### [数据范围]
> 50%的数据:解压后的字符串长度在1,000以内,最多只有三重压缩.
> 100%的数据:解压后的字符串长度在20,000以内,最多只有十重压缩.


- ## [代码]

```c++
#include "stdio.h"
#include "string"
#include "iostream"
using namespace std;

string s;

bool op(int b,int e)
{
    for(int i=b;i<=e;i++)
        if(s[i]=='[')
            return true;
    return false;
}

void DFS(int b,int e)
{
    if(b>e)
        return;
    if(!op(b,e))
        for(int i=b;i<=e;i++)
            cout << s[i];
    else
    {
        int i=b;
        while(s[i]!='[')
        i++;
        int j=i+1,t=1;
        while(t>=1)
        {
            if(s[j]=='[')
                t++;
            if(s[j]==']')
                t--;
            j++;
        }
        j--;
        int n,k;
        for(n=0,k=i+1;s[k]>='0'&&s[k]<='9';k++)
            n=n*10+s[k]-'0';
        DFS(b,i-1);
        while(n--)
            DFS(k,j-1);
        DFS(j+1,e);
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("password.in","r",stdin);
    freopen("password.out","w",stdout);
#endif
    cin >> s;
    DFS(0,s.size()-1);
    return 0;
}
```
