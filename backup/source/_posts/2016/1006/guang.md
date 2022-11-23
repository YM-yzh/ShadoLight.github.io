---
title: 光
date: 2016-10-06 17:17:29
tags: [2016]
categories: daily
ignore: true
---
# 光 ( guang )
---
- ## [问题]

- ### [问题描述]
> 小 S 对神的高傲感到了厌烦,她把神域改造成了一个微型世界,这个世界有 n 个关键点,有 m 条边连接这 n 个关键点,其中每条边都有一个光的通过时间,小 S 会进行测试,将一道圣光沿某条最短的路径从 1 传播到 n,每条边上的微型生命都想看到圣光,他们想知道至少将这条边的光的通过时间缩短多少才能保证看到圣光(此时他们不会考虑其它边的变化).

<!--more-->

- ### [输入格式]
> 第一行两个正整数 n 和 m.接下来 m 行每行三个正整数 u,v,w,表示这条边从 u 指向 v,原先的通过时间为 w.

- ### [输出格式]
> m 行,依次给出每条边的答案,注意缩短的时间必须是整数且缩短后的值必须为正,如果这条边上的人一定见不到圣光则输出-1.

- ### [样例]

>> guang.in | guang.out
>> ---------|----------
>> 3 3 | 0
>> 1 3 2 | 2
>> 1 3 3 | -1
>> 2 3 1 |

- ### [样例解释]
> 边 u=1,v=3,w=2 就是 1 到 3 的最短路,所以缩短的时间为 0;边 u=1,v=3,w=3 必须把 w 缩短 2 后变成 1 才是 1 到 3 的最短路;边 u=2,v=3,w=1 无论 w 怎么缩短都不会变成 1 到 3 的最短路,所以输出-1.

- ### [数据范围]
> 60%的数据:n≤100;
> 80%的数据:n≤1000;
> 100%的数据:n≤10000,w≤10<sup>9</sup>;