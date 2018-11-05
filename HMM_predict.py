# -*- coding:utf-8 -*-
import MP_seg
import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')
with open('pos.txt', 'r') as f:
    pos = [i.strip() for i in f.readlines()]

with open('A.txt', 'r') as f:
    A = json.load(f)

with open('B.txt', 'r') as f:
    B = json.load(f)

with open('words.txt', 'r') as f:
    words = [i.strip() for i in f.readlines()]

with open('fre_pi.txt', 'r') as f:
    fre = {}
    pi = {}
    for i in f.readlines():
        word = i.strip().split(' ')[0]
        fre_ = i.strip().split(' ')[1]
        pi_ = i.strip().split(' ')[2]
        fre[word] = float(fre_)
        pi[word] = float(pi_)

num_pos = len(pos)
num_words = len(words)
string = raw_input('请输入句子:')
segment = MP_seg.Segment()
words_list = segment.segment(string)
words_list_len = len(words_list)
dp = [{} for i in xrange(words_list_len)]
pre = [{} for i in xrange(words_list_len)]
for k in pos:
    for j in range(words_list_len):
        dp[j][k] = 0
        pre[j][k] = ""

for c in pos:
    if (B[c].has_key(words_list[0])):
        dp[0][c] = pi[c] * B[c][words_list[0]]
    else:
        tmp = 1.0 / (fre[c] + num_words)
        dp[0][c] = pi[c] * tmp

for i in range(1, words_list_len):
    for j in pos:
        for k in pos:
            tt = 0
            if (B[j].has_key(words_list[i])):
                tt = B[j][words_list[i]]
            else:
                tt = 1.0 / (fre[j] + num_words)
            if (dp[i][j] < dp[i - 1][k] * A[k][j] * tt):
                dp[i][j] = dp[i - 1][k] * A[k][j] * tt
                pre[i][j] = k

res = {}
MAX = ""
for j in pos:
    if (MAX == "" or dp[words_list_len - 1][j] > dp[words_list_len - 1][MAX]):
        MAX = j
i = words_list_len - 1
while (i >= 0):
    res[i] = MAX
    MAX = pre[i][MAX]
    i -= 1
for i in range(0, words_list_len):
    print words_list[i].decode('utf-8') + "\\" + res[i].decode('utf-8'),
