# -*- coding:utf-8 -*-
import sys
from Tkinter import *

reload(sys)
sys.setdefaultencoding('utf-8')


class Bi_MM():
    def __init__(self):
        self.dictionary = Bi_MM.read_dictionary(self)

    def read_dictionary(self):
        with open('chineseDic.txt', 'r') as f:
            dictionary = [i.strip().split(',')[0].encode('utf-8') for i in f.readlines()]
        return dictionary

    def seg(self, sentence, Maxlength):
        MM_sentence = self.MM(sentence, Maxlength)
        print MM_sentence
        RMM_sentence = self.RMM(sentence, Maxlength)
        print RMM_sentence
        if MM_sentence == RMM_sentence:
            return MM_sentence
        else:
            if len(MM_sentence) > len(RMM_sentence):
                return RMM_sentence
            else:
                return MM_sentence

    def MM(self, sentence, Maxlength):
        Length = Maxlength
        temp_sentence = sentence
        result = ''
        while (len(temp_sentence) > 0):
            temp_word = temp_sentence[:Length]
            if temp_word in self.dictionary:
                result += temp_word
                result += '/'
                temp_sentence = temp_sentence[Length:]
                Length = Maxlength
            else:
                if Length == 1:
                    result += temp_word
                    result += '/'
                    Length = Maxlength
                    temp_sentence = temp_sentence[Length:]
                else:
                    Length = Length - 1

        return result

    def RMM(self, sentence, Maxlength):
        Length = Maxlength
        temp_sentence = sentence
        result = ''
        while (len(temp_sentence) > 0):
            temp_word = temp_sentence[-Length:]
            if temp_word in self.dictionary:
                result = temp_word + '/' + result
                temp_sentence = temp_sentence[:-Length]
                Length = Maxlength
            else:
                if Length == 1:
                    result = temp_word + result
                    result = temp_word + '/' + result
                    temp_sentence = temp_sentence[:-Length]
                else:
                    Length = Length - 1

        return result
