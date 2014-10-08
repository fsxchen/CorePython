"""
	当考虑到使用临界资源的时候，使用锁是很有必要的，下面就使用Lock实现了资源控>
	可以使用with来代替require(),和release() 
"""
from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime

lock = Lock()

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)
loops = (randrange(2,5) for x in xrange(randrange(3,7)))
remaining = CleanOutputSet()
def loop(nsec):
    myname = currentThread().name
    remaining.add(myname)
    lock.acquire()
    print '[%s] Started %s' % (ctime(), myname)
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print '[%s] Completed %s (%d secs)' % ( \
    ctime(), myname, nsec)
    print '(remaining: %s)' % (remaining or 'NONE')
    lock.release()
def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()
@register
def _atexit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    _main()
