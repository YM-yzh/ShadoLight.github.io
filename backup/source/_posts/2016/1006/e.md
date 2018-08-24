---
title: 恶
date: 2016-10-06 14:31:46
tags: [2016]
categories: daily
ignore: true
---
# 恶 ( e )
---
- ## [问题]

- ### [问题描述]
> 有 n 个恶魔就要诞生了,恶魔头子要给每个即将诞生的恶魔取一个名字,恶魔秘书给恶魔头子提供了 n 个字符串供参考,由于每个字符串单词都很长,恶魔头子想到先把单词化简一下,方法是把每个单词尽量取短些的前缀,但所取的前缀不能是其它单词的前缀.这个任务现在就交给你来完成.

<!--more-->

- ### [输入格式]
> 第一行一个整数 N,表示单词个数.下面有 N 行,每行一个单词,每个单词的长度不超过 50,且都是由小写字母组成,保证所给单词没有一个单词是另一个单词的前缀.

- ### [输出格式]
> 共 N 行,每行一个单词,是对应上面的 N 个单词化简后的单词.

- ### [样例]

>> e.in | e.out
>> -----|------
>> 3 | a
>> abc | e
>> efg | i
>> ijh |

- ### [数据范围]
> 100%的数据:1 ≤N ≤50.

- ## [代码]
```c++
#include "stdio.h"
#include "string.h"

const int N=54;

int n;
char name[N][N];
char ans[N],tmp[N];
bool avail;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("e.in","r",stdin);
    freopen("e.out","w",stdout);
#endif
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%s",name[i]);
    for(int i=1;i<=n;i++)
    {
        int len=strlen(name[i]);
        for(int j=1;j<=len;j++)
        {
            strcpy(ans,name[i]);
            ans[j]='\0';
            avail=true;
            for(int k=1;k<=n;k++)
            {
                if(k==i)
                    continue;
                strcpy(tmp,name[k]);
                tmp[j]='\0';
                if(!strcmp(ans,tmp))
                {
                    avail=false;
                    break;
                }
            }
            if(avail)
            {
                printf("%s\n",ans);
                break;
            }
        }
    }
    return 0;
}
```
