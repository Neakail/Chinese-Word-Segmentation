# -*- coding:utf-8 -*-

from Tkinter import *
import Bi_MM
import time
import MP_seg
class Bi_MM_GUI():
    def __init__(self):
        window = Tk()
        window.title('Bi_MM')
        window.geometry('400x300')
        content = Label(window, text='内容')  # 生成标签
        content.pack()
        self.e = Entry(window, width=50)
        self.e.pack()
        length = Label(window, text='长度')  # 生成标签
        length.pack()
        self.e1 = Entry(window, width=50)
        self.e1.pack()
        b1 = Button(window, text='BIMM分词', width=15, height=2, command=self.insert_point)
        b1.pack()
        b2 = Button(window, text='MP分词', width=15, height=2, command=self.insert_point_MP)
        b2.pack()
        result = Label(window, text='结果')  # 生成标签
        result.pack()
        self.t = Text(window, height=5)  # 这里设置文本框高，可以容纳两行
        self.t.pack()
        time = Label(window, text='时间')  # 生成标签
        time.pack()
        self.t1 = Text(window, height=1)  # 这里设置文本框高，可以容纳两行
        self.t1.pack()
        self.seg1 = Bi_MM.Bi_MM()
        self.seg2= MP_seg.Segment()
        window.mainloop()

    def insert_point(self):
        self.t.delete(0.0, END)
        self.t1.delete(0.0,END)
        input_ = self.e.get()
        length = int(self.e1.get())
        starttime = time.time()
        result = self.seg1.seg(input_, length)
        endtime = time.time()
        time_ = endtime - starttime
        self.t.insert('insert', result)
        self.t1.insert('insert',time_)

    def insert_point_MP(self):
        self.t.delete(0.0, END)
        self.t1.delete(0.0,END)
        input_ = self.e.get()
        length = int(self.e1.get())
        starttime = time.time()
        result_ = self.seg2.segment(input_,length)
        result = '/'.join(result_)
        endtime = time.time()
        time_ = endtime - starttime
        self.t.insert('insert', result)
        self.t1.insert('insert',time_)


if __name__ == '__main__':
    Bi_MM_GUI()
