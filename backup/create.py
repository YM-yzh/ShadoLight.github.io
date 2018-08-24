#!/bin/env python

import os
import sys
import datetime

# datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def deal(str):
    return str.replace('？', '?').replace('！', '!').replace('（', '(').replace('）', ')').replace('【', '[').replace('】', ']').replace('；', ';').replace('：', ':')

def when(ENstr):
    print(ENstr + ': (# in a single line represents the end.)')
    readln = deal(sys.stdin.readline().strip())
    f.write("> ")
    while (not readln == '#'):
        f.write(readln)
        readln = deal(sys.stdin.readline().strip())
    f.write('\n')

def xyzsl(ENstr, CNstr):
    readln = input(ENstr + '?(true/false): ')
    if (readln == 'true'):
        print(ENstr + ': (# in a single line represents the end.)')
        f.write('\n- ### [' + CNstr + ']\n')
        readln = deal(sys.stdin.readline().rstrip())
        f.write("> ")
        while not readln == '#':
            f.write(readln)
            readln = deal(sys.stdin.readline().rstrip())
        f.write('\n')


name = input('Chinese Name: ')
nameEN = input('English Name: ')
year = datetime.datetime.now().strftime('%Y')
date = datetime.datetime.now().strftime('%m%d')
time = datetime.datetime.now().strftime('%H:%M:%S')

if (not os.path.exists('source/_posts/' + year + '/' + date)):
    os.makedirs('source/_posts/' + year + '/' + date)
f = open('source/_posts/' + year + '/' + date + '/' + nameEN.lower() + '.md', 'w')

f.write('---\n')
f.write('title: ' + name + '\n')
f.write('date: ' + datetime.datetime.now().strftime('%Y-%m-%d') + ' ' + time + '\n')

f.write('tags: [' + year)
print('Tags: (# in a single line represents the end.)')
tag = sys.stdin.readline().strip()
f.write(', ' + tag)
while (not tag == '#'):
    f.write(', ' + tag)
    tag = sys.stdin.readline().strip()
f.write(']\n')

cate = input('Categories :')
f.write('categories: ' + cate + '\n')
f.write('---\n')

f.write('# ' + name + ' ( ' + nameEN.lower() + ' )\n')
f.write('---\n')

readln = input('Source?' + '(true/false): ')
if (readln == 'true'):
    f.write('\n- ## [来源]\n')
    print('Source: (# in Source Name represents the end.)')
    des = input('Source Name: ')
    web = input('Source Website: ')
    while not des == '#':
        f.write('- @')
        f.write('[' + des + ']')
        f.write('(' + web + ')')
        f.write(' ')
        des = input('Source Name: ')
        web = input('Source Website: ')
    f.write('\n')

f.write('- ## [问题]\n')

f.write('\n- ### [问题描述]\n')
when('Describe')
f.write('\n<!--more-->\n')

f.write('\n- ### [输入格式]\n')
when('Input Format')
f.write('\n- ### [输出格式]\n')
when('Output Format')

cnt = int(input('Quantity of Samples: '))
if (not cnt == 0):
    f.write('\n- ### [样例]\n')
    for i in range(0, cnt):
        sampleIn = []
        sampleOut = []
        inLine = 0
        outLine = 0
        print('Sample Input #' + str(i + 1) + ': (# in a single line represents the end.)')
        readln = sys.stdin.readline().rstrip()
        f.write("> ")
        while (not readln == '#'):
            inLine += 1
            sampleIn.append(readln)
            readln = sys.stdin.readline().rstrip()
        print('Sample Output #' + str(i + 1) + ': (# in a single line represents the end.)')
        readln = sys.stdin.readline().rstrip()
        f.write("> ")
        while (not readln == '#'):
            outLine += 1
            sampleOut.append(readln)
            readln = sys.stdin.readline().rstrip()
        if (cnt == 1):
            f.write('>> ' + nameEN + '.in | ' + nameEN + '.out\n')
            f.write('>> ' + '-' * (len(nameEN) + 4+ len(str(i + 1))) + '|' + '-' * (len(nameEN) + 5 + len(str(i + 1))) + '\n')
        else:
            f.write('>> ' + nameEN + str(i + 1) + '.in | ' + nameEN + str(i + 1) + '.out\n')
            f.write('>> ' + '-' * (len(nameEN) + 4+ len(str(i + 1))) + '|' + '-' * (len(nameEN) + 5 + len(str(i + 1))) + '\n')
        totLine = max(inLine, outLine)
        for j in range(0, totLine):
            if (j >= inLine):
                f.write('>> ' + ' | ' + sampleOut[j] + '\n')
            elif (j >= outLine):
                f.write('>> ' + sampleIn[j] + ' | \n')
            else:
                f.write('>> ' + sampleIn[j] + ' | ' + sampleOut[j] + '\n')
        f.write('\n\n')

    xyzsl('Explain', '样例解释')

xyzsl('Hint', '数据范围')

xyzsl('Limit', '限制')

xyzsl('Analysis', '分析')

readln = input('Code?' + '(true/false): ')
if (readln == 'true'):
    lan = input('Language Mode: ')
    print('Code: (# in a single line represents the end.)')
    f.write('\n- ## [代码]\n')
    f.write('\n```' + lan + '\n')
    readln = sys.stdin.readline().rstrip()
    while not readln == '#':
        f.write(readln)
        f.write('\n')
        readln = sys.stdin.readline().rstrip()
    f.write('\n```\n')

print('Done!')

f.close()
