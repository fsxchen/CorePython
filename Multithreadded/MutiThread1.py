#!/usr/bin/python
#coding:utf-8
"""
	使用thread类实现的多线程，在这里，无法知道主线程在什么时候退出，因此使用了sleep
	在下面的代码中得到了解决
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
