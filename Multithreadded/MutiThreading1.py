#!/usr/bin/python
#coding:utf-8

"""
	ʹ��Threadingģ����ж��̣߳�Ŀǰ�Ƚ��ƽ����һ������ֱ����ʵ������ʱ�򣬸�����
	Ҫ����ĺ����������÷��Ƚϼ򵥣�Ҳ�Ƚϳ���,����Ҫ�Լ�ȥ���õȴ����̵߳�����
	����join()������һ����Բ��ӣ��������߳������������ʱ����Ҫ������һ��Ҫ��

"""
import threading
from time import ctime, sleep

def loop0():
    print 'start loop0 at:', ctime()
    sleep(2)
    print 'loop 0 done at:', ctime()

def loop1():
    print 'start loop1 at:', ctime()
    sleep(4)
    print 'loop1 done at:', ctime()


def main():
    Thread_list = []
    print "This starting at:", ctime()
    t1 = threading.Thread(target=loop0, args=())
    t2 = threading.Thread(target=loop1, args=())
    Thread_list.append(t1)
    Thread_list.append(t2)
    
    for tl in Thread_list:
        tl.start() 
    print "all DONE at:", ctime()

if __name__ == '__main__':
    main()
