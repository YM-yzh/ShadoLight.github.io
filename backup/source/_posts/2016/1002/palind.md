---
title: 回文平方数
date: 2016-10-02 19:52:59
tags: [2016]
categories: daily
ignore: true
---
# 回文平方数 ( palind )
---
- ## [问题]

- ### [描述]
> 回文数是指从左向右读和从右向左读都一样的数.如12321就是一个回文数.
> 现在给定一个进制B(B是十进制),输出所有的大于等于1小于等于300且它的平方用B进制表示时是回文数的数.用" A ","B"……表示10,11等等.

<!--more-->

- ### [输入格式]
> 共一行,一个单独的整数B(B用十进制表示).

- ### [输出格式]
> 每行两个数字(都是B进制数表示),第二个数是第一个数的平方,且第二个数是回文数.

- ### [样例]

>> palind.in | palind.out
>> ----------|-----------
>> 10 | 1 1
>>  | 2 4
>>  | 3 9
>>  | 11 121
>>  | 22 484
>>  | 26 676
>>  | 101 10201
>>  | 111 12321
>>  | 121 14641
>>  | 202 40804
>>  | 212 44944
>>  | 264 69696

- ### [数据范围]
> 100%的数据:2≤B≤20.

- ## [代码]

```c++
#include "stdio.h"
#include "string"
#include "iostream"
#include "algorithm"
using namespace std;

int b;

bool op(string x)
{
    string y=x;
    reverse(y.begin(),y.end());
    return (x==y);
}

char change(int x)
{
    if(x>=10)
        return x-10+'A';
    return x+'0';
}

string toB(int x)
{
    string y;
    while(x)
    {
        y.insert(y.end(),change(x%b));
        x/=b;
    }
    reverse(y.begin(),y.end());
    return y;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("ps.in","r",stdin);
    freopen("ps.out","w",stdout);
#endif
    scanf("%d",&b);
    for(int i=1;i<=300;i++)
    {
        string x=toB(i);
        string y=toB(i*i);
        if(op(y))
            cout << x << ' ' << y << endl;
    }
    return 0;
}
```
