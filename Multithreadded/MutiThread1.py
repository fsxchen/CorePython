#!/usr/bin/python
#coding:utf-8
"""
	ʹ��thread��ʵ�ֵĶ��̣߳�������޷�֪�����߳���ʲôʱ���˳������ʹ����sleep
	������Ĵ����еõ��˽��
"""
import thread
from time import ctime, sleep
from Loop import loop0, loop1

def main():
    print "This starting at:", ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print "all DONE at:", ctime()

if __name__ == '__main__':
    main()
