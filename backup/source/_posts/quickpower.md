---
title: 快速幂
date: 2016-10-03 21:14:00
tags: snippets
categories: algorithm
---
# a<sup>b</sup> mod c
---

<!--more-->

```c++
int QuickPower(int a,int b,int c)
{
    int cnt=1;
    while(b>0)
    {
        if(b&1)
            cnt=(cnt*a)%c;
        a=(a*a)%c;
        b>>=1;
    }
    return cnt;
}
```
