# -*- coding: utf-8 -*-
import time


class Segment(object):

    def __init__(self):
        word_dict = self.get_word_dict()
        self._word_dict = dict(word_dict)
        self._max_len = 0
        for word in self._word_dict:
            self._max_len = max(self._max_len, len(word))

    def segment(self, sentence, max_len=None):

        max_len = self._max_len if max_len is None else max_len
        if max_len <= 0:
            raise Exception('Invalid argument max_len, must be greater than 0')

        if not sentence:
            return []

        if isinstance(sentence, str):
            sentence = sentence.decode('utf-8')

        # 最佳左邻词
        left_words = [u'' for _ in range(len(sentence) + 1)]
        left_words_probabilities = [0 for _ in range(len(sentence) + 1)]
        left_words_probabilities[0] = 1

        for i in range(len(sentence)):
            end = min(len(sentence), i+max_len)
            # 找出候选词，计算其累计概率，更新相应的最佳左邻词
            for j in range(i+1, end + 1):
                word = sentence[i:j]
                if word in self._word_dict:
                    cumulative_probability = left_words_probabilities[i] * self._word_dict[word]
                    # print cumulative_probability
                    if cumulative_probability > left_words_probabilities[j]:
                        left_words[j] = word
                        left_words_probabilities[j] = cumulative_probability
                elif len(word) == 1:
                    cumulative_probability = left_words_probabilities[i] * 0.0000000001
                    # print cumulative_probability
                    if cumulative_probability > left_words_probabilities[j]:
                        left_words[j] = word
                        left_words_probabilities[j] = cumulative_probability


        # 反向导出结果
        i = len(sentence)
        result = []
        while left_words[i]:
            result.append(left_words[i])
            i -= len(left_words[i])

        return tuple(reversed(result))

    @classmethod
    def get_word_dict(cls):
        words = {}
        with open('WordFrequency.txt') as f:
            for line in f.read().decode('utf-8').split():
                line = line[:-1]
                word, _, probability = line.rsplit(',', 2)
                words[word] = float(probability)

        return words


def main():
    segment = Segment()
    start = time.time()
    print '/'.join(segment.segment('杨幂你好啊'))
    print '耗时:%f秒' % (time.time() - start)


