#!/usr/bin/python
#coding:utf-8
"""
	解决了上面的问题，主线程不需要用sleep等待子线程了,但是这种方法需要
	在函数调用时传递一个lock
"""
import thread
from time import ctime, sleep

# from NoMt import loop0, loop1


locks = []

def loop0(lock):
    
    print 'start loop0 at:', ctime()
    sleep(2)
    print 'loop 0 done at:', ctime()
    lock.release()

def loop1(lock):
    
    print 'start loop1 at:', ctime()
    sleep(4)
    print 'loop1 done at:', ctime()
    lock.release()


def main():
    loc1 = thread.allocate_lock()
    loc2 = thread.allocate_lock()
    loc1.acquire()
    loc2.acquire()
    locks.append(loc1)
    locks.append(loc2)
    print "This starting at:", ctime()
    thread.start_new_thread(loop0, (loc1,))
    thread.start_new_thread(loop1, (loc2,))
    for i in range(2):
        while locks[i].locked():
            pass

    print "all DONE at:", ctime()

if __name__ == '__main__':
    main()
