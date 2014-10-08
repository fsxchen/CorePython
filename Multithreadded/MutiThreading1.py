#!/usr/bin/python
#coding:utf-8

"""
	使用Threading模块进行多线程，目前比较推介的这一方法，直接在实例化的时候，给出了
	要处理的函数，这种用法比较简单，也比较常见,不许要自己去设置等待主线程的锁，
	关于join()方法，一般可以不加，但是主线程如果有其他的时间需要处理，则一定要加

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
