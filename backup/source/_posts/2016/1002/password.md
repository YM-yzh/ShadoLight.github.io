---
title: 魔族密码
date: 2016-10-02 11:35:38
tags: [2016]
categories: daily
ignore: true
---
# 魔族密码 ( password )
---
- ## [问题]

- ### [描述]
> 风之子刚走进他的考场,就……
> 花花:当当当当\~~偶是魅力女皇——花花!!^^(华丽出场,礼炮,鲜花)
> 风之子:我呕……(杀死人的眼神)快说题目!否则……
> 花花:……咦\~~好冷~~我们现在要解决的是魔族的密码问题(自我陶醉:搞不好魔族里面还会有人用密码给我和菜虫写情书咧,哦活活,当然是给我的比较多拉.)魔族现在使用一种新型的密码系统.每一个密码都是一个给定的仅包含小写字母的英文单词表,每个单词至少包含1个字母,至多75个字母.如果在一个由一个词或多个词组成的表中,除了最后一个以外,每个单词都被其后的一个单词所包含,即前一个单词是后一个单词的前缀,则称词表为一个词链.例如下面单词组成了一个词链:
> i
> int
> integer
> 但下面的单词不组成词链:
> integer
> intern
> 现在你要做的就是在一个给定的单词表中取出一些词,组成最长的词链,就是包含单词数最多的词链.将它的单词数统计出来,就得到密码了.
> 风之子:密码就是最长词链所包括的单词数阿……
> 花花:活活活,还有,这些文件的格式是,第一行为单词表中的单词数N(1<=N<=2000),下面每一行有一个单词,按字典顺排列,中间也没有重复的单词咧!!你要提交的文件中只要在第一行输出密码就行啦^^看你长得还不错,给你一个样例吧:

<!--more-->

- ### [样例]

>> password.in | passeord.out
>> ------------|-------------
>> 5 | 4
>> i
>> int
>> integer
>> intern
>> internet

- ### [时间限制]
> 各个测试点1s

- ## [代码 ]

```c++
#include "stdio.h"
#include "string"
#include "iostream"
using namespace std;

const int N=2004;

int n;
int f[N],ans;
string s[N];

bool op(string a,string b)
{
    if(a.size()>b.size())
        return false;
    for(int i=0;a[i];i++)
        if(a[i]!=b[i])
            return false;
    return true;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("password.in","r",stdin);
    freopen("password.out","w",stdout);
#endif
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        cin >> s[i];
    f[1]=1;
    for(int i=2;i<=n;i++)
    {
        f[i]=1;
        for(int j=i-1;j>=1;j--)
            if(op(s[j],s[i]))
                f[i]=max(f[i],f[j]+1);
        ans=ans>f[i]?ans:f[i];
    }
    printf("%d\n",ans);
    return 0;
}
```
