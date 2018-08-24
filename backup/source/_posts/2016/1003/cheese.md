---
title: 奶酪
date: 2016-10-03 09:35:44
tags: [2016]
categories: daily
ignore: true
---
# 奶酪 ( cheese )
---
## 总时间限制: 100ms | 内存限制: 65536kB

- ## [问题]

- ### [描述]
> 阿尔吉侬是一只聪明又慵懒的小白鼠,它最擅长的就是走各种各样的迷宫.今天它要挑战一个非常大的迷宫,研究员们为了鼓励阿尔吉侬尽快到达终点,就在终点放了一块阿尔吉侬最喜欢的奶酪.现在研究员们想知道,如果阿尔吉侬足够聪明,它最少需要多少时间就能吃到奶酪.
> 迷宫用一个R×C的字符矩阵来表示.字符S表示阿尔吉侬所在的位置,字符E表示奶酪所在的位置,字符#表示墙壁,字符.表示可以通行.阿尔吉侬在1个单位时间内可以从当前的位置走到它上下左右四个方向上的任意一个位置,但不能走出地图边界.

<!--more-->

- ### [输入格式]
> 第一行包含了两个用空格分开的正整数R和C(2 <= R, C <= 200),表示地图是一个R×C的矩阵.
> 接下来的R行描述了地图的具体内容,每一行包含了C个字符.字符含义如题目描述中所述.保证有且仅有一个S和E.

- ### [输出格式]
> 对于每一组数据,输出阿尔吉侬吃到奶酪的最少单位时间.若阿尔吉侬无法吃到奶酪,则输出“oop!”(只输出引号里面的内容,不输出引号).每组数据的输出结果占一行.

- ### [样例]

>> cheese1.in | cheese1.out
>> -----------|------------
>> 3 4 | 5
>> .S.. |
>> ###. |
>> ..E. |

cheese2.in | cheese2.out
-----------|------------
3 4 | 1
.S.. |
.E.. |
.... |

cheese3.in | cheese3.out
-----------|------------
3 4 | oop!
.S.. |
#### |
..E. |

- ## [代码]

```c++
#include "deque"
#include "iostream"
#include "algorithm"
using namespace std;

const int N=204;
const int X[4]={ 0, 0, 1,-1};
const int Y[4]={ 1,-1, 0, 0};

struct XOY
{
    int x,y;
    int s;
}b,e;

int n,m;
bool a[N][N],v[N][N];
deque<XOY> q;

void BFS(XOY x)
{
    q.push_back(x);
    while(q.size())
    {
        XOY o=q.front();
        q.pop_front();
        for(int i=0;i<4;i++)
        {
            int xx=o.x+X[i],yy=o.y+Y[i];
            if(xx<1 or xx>n or yy<1 or yy>m)
                continue;
            if(v[xx][yy] or a[xx][yy])
                continue;
            v[xx][yy]=true;
            if(xx==e.x and yy==e.y)
            {
                cout << o.s+1 << endl;
                return ;
            }
            q.push_back((XOY){xx,yy,o.s+1});
        }
    }
    puts("oop!");
}

int main()
{
    cin >> n >> m;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            char c;
            cin >> c;
            if(c=='S')
                b.x=i,b.y=j;
            if(c=='E')
                e.x=i,e.y=j;
            a[i][j]=(c=='#');
        }
    }
    BFS(b);
    return 0;
}
```
