def foo():
    print('Foo')

def bar():
    print('Bar')

from threading import Thread

t1 = Thread(target=foo)
t1.start()

t2 = Thread(target=bar)
t2.start()