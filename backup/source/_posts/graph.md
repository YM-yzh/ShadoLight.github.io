---
title: 图论
date: 2016-10-04 11:15:19
tags: snippets
categories: algorithm
---
# 图论
---

<!--more-->

- ## 存储

- ### 邻接矩阵
```c++
// 从u到v有一条权值为w的边
void add(int u,int v,int w)
{
    G[a][b]=c;
}
```

- ### 邻接表
```c++
// 从u到v有一条权值为w的边
void add(int u,int v,int w)
{
    tnt++;
    next[tnt]=first[u];
    first[u]=tnt;
    weight[tnt]=a;
    end[tnt]=j;
}
```

- ## 遍历

- ### 深度优先

```c++
void DFS(int u)
{
    if(vis[u])
        return ;
    vis[u]=true;
    for(int e=first[u];e;e=next[e])
        DFS(end[e]);
}
```
<!--
- ### 广度优先

```c++
void BFS()
{

}
``` -->
