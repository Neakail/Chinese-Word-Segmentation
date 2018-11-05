# -*- coding: UTF-8 -*-

import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')


# 所有词语
words = []
# 所有的词性
pos = []
# 每个词性出现的频率
fre = {}
# 先验概率矩阵
pi = {}
# 状态转移概率矩阵
A = {}
# 观测概率矩阵
B = {}

with open('199801_1.txt', 'r') as f:
    for line in f.readlines():
        if line.strip() == '':
            continue
        else:
            tmp = line.strip().split(' ')
            n = len(tmp)
            for word_pos in xrange(1, n):
                word = tmp[word_pos].split('/')[0]
                pos_ = tmp[word_pos].split('/')[1]
                if pos_ not in pos:
                    pos.append(pos_)
                if word not in words:
                    words.append(word)

num_pos = len(pos)
num_words = len(words)

# 初始化概率矩阵
for i in pos:
    pi[i] = 0
    fre[i] = 0
    A[i] = {}
    B[i] = {}
    for j in pos:
        A[i][j] = 0
    for j in words:
        B[i][j] = 0

count = 0
with open('199801_1.txt', 'r') as f:
    for line in f.readlines():
        if line.strip() == '':
            continue
        else:
            count += 1
            tmp = line.strip().split(' ')
            n = len(tmp)
            for word_pos in xrange(1, n):
                word = tmp[word_pos].split('/')[0]
                pos_ = tmp[word_pos].split('/')[1]
                pre_word = tmp[word_pos - 1].split('/')[0]
                pre_pos_ = tmp[word_pos - 1].split('/')[1]
                fre[pos_] += 1
                if word_pos == 1:
                    pi[pos_] += 1
                else:
                    A[pre_pos_][pos_] += 1
                B[pos_][word] += 1

for i in pos:
    pi[i] = pi[i] * 1.0 / count
    for j in words:
        B[i][j] = (B[i][j] + 1) * 1.0 / (fre[i] + num_words)
    for j in pos:
        A[i][j] = (A[i][j] + 1) * 1.0 / (fre[i] + num_pos)

with open('words.txt', 'w') as f:
    for i in words:
        f.write(i + '\n')

with open('pos.txt', 'w') as f:
    for i in pos:
        f.write(i + '\n')

with open('fre_pi.txt', 'w') as f:
    for i in fre:
        f.write(i + ' ' + str(fre[i]) + ' ' + str(pi[i]) + '\n')

with open('A.txt', 'w') as f:
    json.dump(A, f)

with open('B.txt', 'w') as f:
    json.dump(B, f)
