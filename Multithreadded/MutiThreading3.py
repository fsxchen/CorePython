#!/usr/bin/python
#coding:utf-8

"""
	�Լ���дThread�࣬ע���ڼ̳е�ʱ����Ҫ�̳г���(threading.Thread)�Ĺ��췽��
	��Ҫ��ɵ�������run������ȥʵ�֣��Ƚ����
	��start()��ʱ�򣬿�ʼִ��
"""
import threading
from time import sleep, ctime

loops = (4, 2)

class MyThread(threading.Thread):
    """docstring for MyThread"""
    def __init__(self, func, args, name=""):
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print "start loop", nloop, 'at:', ctime()
    sleep(nsec)
    print "loop", nloop, "done at:", ctime()

def main():
    print "starting at:", ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

if __name__ == '__main__':
    main()